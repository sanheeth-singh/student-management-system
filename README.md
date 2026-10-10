![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
# Student Record Management System

A command-line interface (CLI) application built with Python to manage student records, persist structured data, and handle runtime exceptions gracefully.

> **Note:** Developed as part of **Task 2: Functions, Files & Exception Handling** during the **Codomax Internship**.

---

## What It Does

- **Full CRUD Operations**: Create, read, update, and delete student records.
- **Dual Data Persistence**: Stores primary data in JSON format (`data/students.json`) and supports data export to CSV (`data/students.csv`).
- **Data Filtering & Analytics**: Employs list comprehensions and lambda functions to filter honor roll candidates and rank students by GPA.
- **Robust Exception Handling**: Uses `try-except-finally` blocks and custom exception classes to catch invalid inputs, duplicate IDs, missing records, and file I/O errors.

---

## Project Structure

```text
student-record-system/
├── data/
│   ├── students.json      # Persistent storage
│   └── students.csv       # Export destination
├── src/
│   ├── __init__.py
│   ├── student_manager.py # CRUD & file handling logic
│   └── utils.py           # Custom exceptions & validators
├── main.py                # Interactive CLI menu
├── .gitignore
└── README.md
```
---
## Set-up & Execution
### 1. Clone Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/student-record-system.git
cd student-record-system
```
### 2. Set-up Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```
### 3. Run the Application
```
python main.py
```
