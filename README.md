# SaltBae
### Heuristic Password Dictionary Generator for Security Assessments

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black?style=flat-square&logo=flask)
![Security](https://img.shields.io/badge/Cybersecurity-Password%20Auditing-red?style=flat-square)


SaltBae is a privacy first password dictionary generation tool that creates highly targeted password candidates using contextual information, heuristic mutations, and real world password patterns.

Unlike traditional brute force approaches that generate millions of low probability combinations, SaltBae focuses on generating passwords that users are statistically more likely to create based on personal information, naming habits, dates, and common password construction patterns.
---
## Live Demo

🌐 https://iahsan.pythonanywhere.com
---
---
## 📂 Project Structure

```text
SaltBae/
│
├── app.py
├── logic.py
├── README.md
│
├── static/
│     └──cs
|        └──style.css
|     └──js
|        └──main.js
├── templates/
│   └── index.html
│
└── 100k-most-used-passwords-NCSC.txt
```
---

## 🛠 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SaltBae.git

cd SaltBae
```

### Install Dependencies

```bash
pip install flask
```

### Run Application

```bash
python app.py
```

Application will start on:

```text
http://127.0.0.1:5000
```

---

## 🔄 Processing Workflow

```text
User Input
      │
      ▼
Tokenization Engine
      │
      ▼
Heuristic Mutation Engine
      │
      ▼
Leetspeak & Reverse Mutations
      │
      ▼
Pattern Generation
      │
      ▼
Merge with NCSC Top Passwords
      │
      ▼
Length Filtering
      │
      ▼
Generated Dictionary
```

---
##  Features

### Smart Heuristic Generation

Generate password candidates from:

- First Name
- Last Name
- Partner Name
- Pet Name
- Company / College
- Hometown
- Favorite Color
- Hobbies
- Birth Year
- Important Dates
- Custom Keywords

---

### Intelligent Mutations

#### Word Transformations

```text
ahsan
Ahsan
AHSAN
```

#### Reverse Mutations

```text
ahsan
nasha
```

#### Leetspeak Conversions

```text
ahsan
@h$@n
```

#### Number Combinations

```text
ahsan1999
1999ahsan
```

#### Symbol-Based Patterns

```text
ahsan@1999
ahsan1999!
ahsan#786
```

#### Multi-Word Combinations

```text
ahsanahmad
ahsan_ahmad
ahsanahmad1999
```

---

##  Why SaltBae?

Large password lists such as RockYou contain millions of passwords but often perform poorly during targeted security assessments where contextual information about the user is available.

People rarely choose completely random passwords.

Common examples include:

```text
John@1998
Max123
Delhi#786
Cyber2025
```

SaltBae focuses on these predictable human behaviors to create concise, high-value dictionaries with significantly higher success probability than generic wordlists.

---

##  Heuristic Engine

The generation engine follows a probability first strategy:

### H1 — Base Words

```text
ahsan
cyber
volleyball
```

### H2 — Word + Number

```text
ahsan1999
1999ahsan
```

### H3 — Word + Symbol + Number

```text
ahsan@1999
cyber#786
```

### H4 — Word + Common Suffixes

```text
ahsan123
cyber2025
```

### H5 — Word + Symbol + Common Suffixes

```text
ahsan@123
cyber#2025
```

### H6 — Word Combinations

```text
ahsancyber
ahsan_cyber
```

### H7 — Multi-Word + Number Patterns

```text
ahsancyber1999
ahsancyber@1999
```

---



---

## ⚙️ Technology Stack

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- NCSC Top 100k Password Dataset




## 📊 Example

### Input

```text
First Name: Admin
Birth Year: 1999
Hobby: Cyber
Custom Keyword: !
```

### Sample Output

```text
Admin1999
admin@1999
Admin!
Cyber1999
cyber_admin
rebyc1999
@dm1n
Admin123
CYBER2025
```

---

## 🔍 Core Capabilities

- Context-aware password generation
- CamelCase tokenization
- Reverse string mutations
- Leetspeak transformations
- Symbol insertion patterns
- Multi-word password construction
- Length-based filtering
- Integration with NCSC Top 100k Password Dataset
- Duplicate removal and optimization
- Privacy-first local processing

---

## 🔒 Ethical Use

SaltBae is intended for:

- Password auditing
- Security assessments
- Authorized penetration testing
- Red Team exercises
- Security awareness training
- Capture The Flag (CTF) competitions

Users are responsible for ensuring all activities are authorized and comply with applicable laws and organizational policies.

---

## 🎓 Educational Purpose

This project demonstrates:

- Password pattern analysis
- Heuristic wordlist generation
- Human password behavior modeling
- OSINT-based password prediction concepts
- Secure software development with Python and Flask

---

##  Contributing

Contributions, bug reports, feature requests, and heuristic improvements are welcome.

```bash
git checkout -b feature/new-heuristic

git commit -m "Added new password mutation strategy"

git push origin feature/new-heuristic
```
## Privacy

SaltBae does not store, transmit, or persist user-provided information.

All password generation is performed in-memory during the request lifecycle, and user inputs are discarded once the response is returned.

## 👨‍💻 Author

**Ahsan**

Cybersecurity Researcher • Security Engineering Enthusiast • Python Developer

> "Generate smarter dictionaries, not bigger ones."
