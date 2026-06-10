#  SaltBae
> **🚧 Work in Progress:** SaltBae is currently under active development and will be live soon!

> A Privacy-First Targeted Password Profiler and Risk Assessment Utility.

**SaltBae** is an educational cybersecurity tool designed to demonstrate how easily passwords can be compromised when they are based on predictable personal information. By simulating a targeted custom dictionary attack (similar to tools like CUPP), SaltBae generates a customized wordlist from user inputs and tests a given password against it.

---

## 🚀 Features

*   **Custom Wordlist Generation:** Takes various user inputs (names, important dates, pet names, hobbies, etc.) and uses a mutation engine to combine them into an extensive, targeted password dictionary.
*   **Targeted Risk Analysis:** Allows users to input a test password to see if it gets caught in the generated custom wordlist. 
*   **100% Privacy-First (Client-Side):** Security is paramount. All data collection, wordlist generation, and password testing happen entirely in the browser. **No Personally Identifiable Information (PII) or passwords ever leave your device.**
*   **Modern UI/UX:** Built with Next.js and Tailwind CSS for a seamless, fast, and responsive user experience.

---

## 🛠️ How It Works

SaltBae operates in three simple steps:

1.  **The Input Phase:** The user enters personal details, keywords, numbers, and significant dates into the dynamic form. 
2.  **The Mutation Engine:** The application processes these inputs, applying common password creation patterns (combinations, reversing, appending dates, basic leetspeak) to generate a massive custom dictionary of potential passwords.
3.  **The Test Phase:** The user inputs a password they want to test. SaltBae scans the generated dictionary to check for a match. If a match is found, the password is highly vulnerable to a targeted attack.

---


## ⚙️ Getting Started

To run this project locally on your machine, follow these steps:

