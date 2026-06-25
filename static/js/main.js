document.getElementById('saltbaeForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const fields = [
        'firstName', 'lastName', 'partnerName', 'petName',
        'birthYear', 'importantDate', 'companyCollege',
        'hometown', 'color', 'hobby', 'commonField', 'passwordLength'
    ];

    const payload = {};
    fields.forEach(field => {
        payload[field] = String(document.getElementById(field).value).trim();
    });

    const resultsContainer = document.getElementById('resultsContainer');
    const errorContainer  = document.getElementById('errorContainer');
    const submitBtn       = document.getElementById('submitBtn');
    const progressBar     = document.getElementById('progressBar');

    // Reset UI state
    resultsContainer.classList.add('hidden');
    errorContainer.classList.add('hidden');
    errorContainer.textContent = '';
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="animate-pulse">Compiling...</span>';
    progressBar.classList.remove('hidden');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            // Update stat cards
            document.getElementById('countWord').textContent      = data.count.toLocaleString();
            document.getElementById('heuristicCount').textContent = data.heuristic_count.toLocaleString();
            document.getElementById('ncscCount').textContent      = data.ncsc_count.toLocaleString();
            document.getElementById('totalCount').textContent     = data.count.toLocaleString();

            // Render password list
            const listContainer = document.getElementById('passwordList');
            listContainer.innerHTML = '';

            data.passwords.forEach(pwd => {
                const div = document.createElement('div');
                div.className = 'pwd-item';
                div.textContent = pwd;
                div.title = 'Click to copy';
                div.addEventListener('click', () => {
                    navigator.clipboard.writeText(pwd).then(() => {
                        div.textContent = '✓ Copied';
                        div.classList.add('copied');
                        setTimeout(() => {
                            div.textContent = pwd;
                            div.classList.remove('copied');
                        }, 1200);
                    });
                });
                listContainer.appendChild(div);
            });

            document.getElementById('exportBtn').classList.remove('hidden');
            resultsContainer.classList.remove('hidden');

        } else {
            errorContainer.textContent = '⚠ ' + (data.error || 'Something went wrong.');
            errorContainer.classList.remove('hidden');
        }

    } catch (err) {
        errorContainer.textContent = '⚠ Network error: ' + err.message;
        errorContainer.classList.remove('hidden');
        console.error(err);
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = 'Compile Dictionary';
        progressBar.classList.add('hidden');
    }
});


// Export as .txt
document.addEventListener('click', function (e) {
    if (e.target && e.target.id === 'exportBtn') {
        const items = document.querySelectorAll('#passwordList .pwd-item');
        const text  = Array.from(items).map(d => d.textContent).join('\n');
        const blob  = new Blob([text], { type: 'text/plain' });
        const url   = URL.createObjectURL(blob);
        const a     = document.createElement('a');
        a.href      = url;
        a.download  = 'saltbae_wordlist.txt';
        a.click();
        URL.revokeObjectURL(url);
    }
});