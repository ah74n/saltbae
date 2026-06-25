# SaltBae 🧂 | Heuristic Password Dictionary Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey?style=flat-square&logo=flask)
![Security](https://img.shields.io/badge/Security-Red_Team%20%2F%20Blue_Team-red?style=flat-square)

SaltBae is a localized, privacy-first cybersecurity utility designed to generate highly targeted password dictionaries based on personal and contextual heuristics. It simulates how an attacker might build a probability-based cracking list without creating billions of useless combinations, making it an excellent tool for defensive risk assessment and password policy auditing.

## ⚠️ Responsible Use Policy
**Intended Use:** This tool is developed strictly for educational purposes, security research, CTF (Capture The Flag) events, and authorized defensive risk assessment. 
**Disclaimer:** Any misuse of this tool to generate dictionaries for unauthorized access or malicious attacks is strictly prohibited. The developer assumes no liability for damage caused by the misuse of this software.

---

## ⚡ Core Features

* **Smart Tokenizer:** Automatically splits compound inputs (e.g., CamelCase, comma-separated, space-separated) into individual base words before running heuristics.
* **11-Point Heuristic Engine:** Processes inputs across Identity, Dates, Context, and Custom variables, applying intelligent combinations (Word + Symbol + Number) rather than blind permutation.
* **Leetspeak & Mutation Engine:** Automatically applies common Leetspeak substitutions, reverse strings, and capitalization mutations (lowercase, Capitalized, UPPERCASE).
* **NCSC 100k Integration:** Seamlessly merges generated heuristic passwords with the National Cyber Security Centre's top 100k breached passwords to ensure base coverage.
* **Privacy-First Architecture:** Runs entirely on your local machine (`localhost`). No PII (Personally Identifiable Information) ever leaves your environment.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, Vanilla JavaScript, Custom CSS
* **Data Structures:** Heavily utilizes Python `sets` for automatic O(1) deduplication during dictionary generation.

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ah74n/saltbae.git](https://github.com/ah74n/saltbae.git)
   cd saltbae