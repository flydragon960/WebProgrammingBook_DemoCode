# WebProgrammingBook_DemoCode
# Web Programming: With Modern Full-Stack Technology — Demo Code

Companion source code for the textbook **_Web Programming: With Modern Full-Stack Technology_ (Second Edition)** by **Dr. Yuhong Yan**, Department of Computer Science and Software Engineering, **Concordia University**.

This repository contains all the runnable examples from the book — front end to back end — so you can read a concept, then run and modify the real code beside it.

> A concise, practical, instructor-tested guide to full-stack web development: **HTML5, CSS3, JavaScript, the DOM, Node.js, Python & Flask, web security (JWT)** — and **coding in the AI era**.

---

## 📖 About the book

The book takes you through the complete stack, one layer at a time, with short explanations and lots of real examples. The **Second Edition** adds a Python/Flask back-end track, a dedicated chapter on authentication and security, and an **"In the AI Era"** section in every chapter that teaches you not just how to *write* web code, but how to **read, judge, debug, and secure** the code an AI assistant generates — the skill that matters most today.

It is the official textbook for **SOEN 287 – Web Programming** at Concordia University, and works equally well for **self-learners** and anyone who wants to become a **full-stack developer**.

### 🛒 Get the book
Available on **Amazon** — search for the title and author, or use the link below (make sure you get the **Second Edition**):

- **Amazon:** [Web Programming: With Modern Full Stack Technology](https://www.amazon.ca/Web-Programming-Modern-Stack-Technology/dp/B0HFD6JK5B/ref=sr_1_1?crid=3V82MWPT00AQ9&dib=eyJ2IjoiMSJ9.BK870lBAPXr3bTgSfTgFLZNjt2auXUs0kcSHRrIy1sPGjHj071QN20LucGBJIEps.iqcG29m_-Y4cwY-IgJG6IYl64cDRAu2v4QujYH9rD5I&dib_tag=se&keywords=yuhong+yan&qid=1789478706&sprefix=yuhong%2Caps%2C126&sr=8-1)

---

## 👥 Who this is for

- **SOEN 287 students** — run the examples that go with each lecture and chapter.
- **Self-learners and career-changers** — a guided path from your first HTML page to a deployed full-stack app.
- **Aspiring full-stack developers** — one place to see the front end and back end working together.
- **Instructors** — free, ready-to-run examples for the classroom (slides and exercises available on request — see below).

---

## 🗂️ What's in this repository

The examples are organized **by chapter**. Each chapter folder holds the self-contained examples for that chapter.

| Chapter | Topic | Stack |
|--------:|-------|-------|
| 1 | Fundamentals — the Internet, the Web, HTTP | — |
| 2 | HTML5 | HTML |
| 3 | CSS3 | CSS |
| 4 | JavaScript | JavaScript |
| 5 | Dynamic HTML and the DOM | JavaScript |
| 6 | Server-side programming with Node.js | Node.js |
| 7 | Secure web applications with JSON Web Tokens (JWT) | Node.js |
| 8 | Python fundamentals | Python |
| 9 | Server-side web programming with Flask | Python / Flask |

_(Folder names may differ slightly — open a chapter folder to see its examples and any local `README`.)_

---

## 🚀 Getting started

Clone the repository:

```bash
git clone https://github.com/flydragon960/WebProgrammingBook_DemoCode.git
cd WebProgrammingBook_DemoCode
```

### Prerequisites
- A **modern web browser** (Chrome, Firefox, Edge, or Safari) — for the front-end chapters.
- **Node.js** (v18 or newer) and **npm** — for the Node.js chapters (6–7).
- **Python 3** (3.10 or newer) and **pip** — for the Python/Flask chapters (8–9).
- No database is required — the examples use simple file/JSON storage.

### Front-end examples (Chapters 2–5: HTML, CSS, JavaScript, DOM)
Just open the `.html` file in your browser. For examples that load other files, serve the folder with a tiny local server:

```bash
# from inside the example folder
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

### Node.js examples (Chapters 6–7)
```bash
cd chapterXX-...        # the chapter/example folder
npm install             # if a package.json is present
node server.js          # or the file named in the example
# then open the URL printed in the terminal (e.g. http://localhost:3000)
```

### Python / Flask examples (Chapters 8–9)
```bash
cd chapterXX-...        # the chapter/example folder
python3 -m venv venv && source venv/bin/activate   # optional but recommended
pip install flask       # (plus anything listed in requirements.txt)
python app.py           # or: flask run
# then open http://localhost:5000
```

> **Security note:** these are teaching examples. Any secret keys shown in the code are placeholders — in a real app, load them from **environment variables**, never commit secrets, and turn **off** debug mode before deploying.

---

## 🤖 The "In the AI Era" theme

Every chapter in the book ends with an **"In the AI Era"** section. As you work through this code, don't just run it — **read it and judge it**: Is it correct? What edge case does it miss? Where's the security hole? That habit — *code judgment over code production* — is the whole point of the book.

---

## 🎓 For instructors

Lecture slides, practice assignments, and sample exams are available **on request**. If you are using this book in a course, please contact the author.

---

## 🐛 Found a bug or a typo?

Please [open an issue](https://docs.google.com/forms/d/e/1FAIpQLSdyAkIUzDQXbrUjlgnlaUpjTId3V-47MQY8AR0w3i_voSqb8A/viewform) describing the chapter, the example, and what you saw. Corrections and suggestions are welcome.

---

## 📜 License & usage

This code is provided for **learning and teaching** alongside the book. You are welcome to run, study, and adapt the examples for personal and classroom use. Please keep the attribution to the book and author.

---

## ✍️ Author

**Dr. Yuhong Yan** — Associate Professor, Computer Science and Software Engineering, Concordia University, Montréal.
Web programming instructor since 2008.

---

_If this repository helps you, a ⭐ on the repo — and a review of the book on Amazon — is much appreciated._
