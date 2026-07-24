<div align="center">

# 🎓 Student Management System

### A Modular Student Management System built with **Python** & **SQLite**

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=00C4FF&center=true&vCenter=true&width=600&lines=Student+Management+System;Python+%2B+SQLite+Project;CRUD+%7C+Search+%7C+Statistics;CSV+Export+%7C+Backup+%26+Restore;Designed+with+Modular+Architecture" />
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)

![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge)

![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

![Version](https://img.shields.io/badge/Version-v2.0.0--Alpha-orange?style=for-the-badge)

![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

</div>

---

# 📖 About the Project

The **Student Management System** is a modular command-line application developed using **Python** and **SQLite** to simplify student record management.

The project follows a clean and scalable architecture where each module has a single responsibility. It demonstrates database management, file handling, validation, modular programming, and clean code practices.

This project was built as a learning project to strengthen Python programming and software engineering concepts while creating a portfolio-ready application.

---

# ✨ Features

- ➕ Add Student Records
- 👀 View Student Details
- ✏️ Update Student Information
- 🔍 Search Students
- 🗑️ Delete Student Records
- 📊 Statistics Dashboard
- 📈 Sort Student Data
- 📄 Export Database to CSV
- 💾 Backup Database
- ♻️ Restore Database
- 📂 View Available Backups
- ❌ Delete Backup Files
- ✅ Input Validation
- 🗄️ SQLite Database Integration
- 🧩 Modular Project Structure

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| SQLite3 | Database |
| CSV | Data Export |
| shutil | Backup & Restore |
| os | File Management |
| time | Performance Measurement |
| Modular Programming | Code Organization |

---

# 🏗️ Project Architecture

```text
                   Student Management System
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   Validation           Business Logic        Database
   (validators)            (main.py)        (SQLite3)
        │                    │
        │                    │
        ▼                    ▼
  Helper Functions      Export & Backup
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
        CSV Export                    Database Backup
```

---

# 📂 Project Structure

```text
student-management-system/
│
├── database/
│   ├── database.py
│   └── student.db
│
├── exports/
│   └── export_csv.py
│
├── backup/
│   └── backup_restore.py
│
├── utils/
│   ├── helpers.py
│   └── validator.py
│
├── backups/
│   └── *.db
│
├── config.py
├── main.py
├── README.md
└── LICENSE
```

---

# 📊 Current Project Progress

| Module | Status |
|---------|:------:|
| SQLite Database | ✅ |
| CRUD Operations | ✅ |
| Search | ✅ |
| Statistics Dashboard | ✅ |
| Sorting | ✅ |
| CSV Export | ✅ |
| Backup & Restore | ✅ |
| Validation | ✅ |
| Documentation | 🟡 |
| Logging | 🔜 |
| Unit Testing | 🔜 |

---

# 🚀 Current Version

```text
Version      : v2.0.0-alpha

Project Type : Command Line Application

Language     : Python

Database     : SQLite3

Architecture : Modular

Status       : Active Development
```

---

<div align="center">

### ⭐ If you like this project, consider giving it a Star!

**Made with ❤️ using Python**

</div>