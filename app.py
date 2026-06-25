import os
from flask import Flask, render_template, request, jsonify
from logic import generate_heuristic_dict

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Load NCSC 100k wordlist once at startup into a set.
# ---------------------------------------------------------------------------
NCSC_WORDLIST = set()
NCSC_FILE = os.path.join(os.path.dirname(__file__), '100k-most-used-passwords-NCSC.txt')

try:
    with open(NCSC_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            if word:
                NCSC_WORDLIST.add(word)
    print(f"[SaltBae] Loaded {len(NCSC_WORDLIST)} passwords from NCSC wordlist.")
except FileNotFoundError:
    print(f"[SaltBae] WARNING: NCSC wordlist not found at {NCSC_FILE}. Continuing without it.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data received.'}), 400

        # Step 1: Heuristic list from personal info
        heuristic_passwords = set(generate_heuristic_dict(data))

        # Step 2: Merge with NCSC list — set union deduplicates automatically
        master_list = heuristic_passwords | NCSC_WORDLIST

        # Step 3: Apply length filter to master list too if provided
        length_raw = (data.get('passwordLength') or '').strip()
        filtered_list = master_list

        if length_raw:
            import re
            range_match = re.match(r'^(\d+)\s*[-]\s*(\d+)$', length_raw)
            single_match = re.match(r'^(\d+)$', length_raw)
            if range_match:
                lo, hi = int(range_match.group(1)), int(range_match.group(2))
                lo, hi = min(lo, hi), max(lo, hi)
                filtered_list = {p for p in master_list if lo <= len(p) <= hi}
            elif single_match:
                n = int(single_match.group(1))
                filtered_list = {p for p in master_list if len(p) == n}

        return jsonify({
            'count': len(filtered_list),
            'heuristic_count': len(heuristic_passwords),
            'ncsc_count': len(NCSC_WORDLIST),
            'passwords': sorted(filtered_list)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)