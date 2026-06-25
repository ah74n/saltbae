# SaltBae 🧂 | Heuristic Password Dictionary Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey?style=flat-square&logo=flask)
![Security](https://img.shields.io/badge/Security-Red_Team%20%2F%20Blue_Team-red?style=flat-square)

SaltBae is a localized, privacy-first cybersecurity utility designed to generate highly targeted password dictionaries based on personal and contextual heuristics. It simulates how an attacker might build a probability-based cracking list without creating billions of useless combinations.

## 🎯 Why is this useful for Password List Generation?
Standard, massive wordlists (like `rockyou.txt`) are great for broad attacks, but they often fail during **targeted risk assessments** or specific CTF scenarios where a user's personal context is key. 

When people create passwords, they rarely use pure randomness. Instead, they rely on predictable patterns—combining their pet's name with a birth year, or their hometown with a special character. 

**SaltBae solves this by:**
1. Taking targeted OSINT data (names, hobbies, important dates, companies).
2. Applying intelligent permutations (e.g., `Word + Symbol + Number`) instead of blind brute-force generation.
3. Outputting a highly probable, concise `.txt` wordlist that is optimized for tools like **Hashcat** or **Hydra**, drastically reducing cracking time during audits.

## 🚀 Installation & Usage

To keep your personal data secure, SaltBae is designed to be run entirely on your local machine (`localhost`). No data is sent over the internet.

### Prerequisites
* Python 3.x installed on your system.
* Git installed.

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ah74n/saltbae.git](https://github.com/ah74n/saltbae.git)
   cd saltbae