<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#4ade80&height=180&section=header&text=Venv%20Doctor&fontSize=42&fontColor=ffffff" alt="Venv Doctor banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=4ADE80&center=true&vCenter=true&width=650&lines=Know%20which%20Python%20and%20pip%20your%20terminal%20is%20using." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/venv-doctor?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/venv-doctor?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/venv-doctor?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/venv-doctor?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Venv Doctor illustration"/></p>

## 🚀 Overview

Venv Doctor is a local diagnostic CLI for confusing Python setups. It reports the active interpreter, virtual-environment state, VIRTUAL_ENV consistency, pip availability, and site-packages path without installing or changing anything.

## ✨ Features

- 🐍 Show the exact Python executable and version
- 🧪 Detect mismatches between VIRTUAL_ENV and sys.prefix
- 📦 Check pip through the active interpreter
- 🛡️ Run diagnostics without modifying the environment

## 🎬 Demo

~~~bash
python main.py --json
~~~

The report is generated locally and does not install or update packages.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/venv-doctor.git
cd venv-doctor
python main.py
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
venv-doctor/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working environment diagnostics
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional exportable environment snapshot
- [ ] 🧰 More platform-specific checks

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#4ade80,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
