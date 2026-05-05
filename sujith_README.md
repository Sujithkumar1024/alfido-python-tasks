# 🐍 Alfido Tech – Python Developer Internship Tasks

**Intern:** Sujithkumar1024  
**Internship:** Alfido Tech – Python Developer Track  
**Tasks Completed:** Task 1, Task 2, Task 4

---

## 📁 Project Structure

```
alfido-python-tasks/
├── task1_file_handling.py       # Task 1: File Handling & Automation
├── task2_api_integration.py     # Task 2: API Integration & JSON Handling
├── flask_app/                   # Task 4: Flask Mini Project
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── add.html
│       └── edit.html
```

---

## ✅ Task 1 – Python File Handling & Automation

**Concepts:** File I/O, CSV, JSON, Exception Handling, Automation

**Features:**
- Read and write text files with exception handling
- CSV creation and parsing using `csv.DictReader`
- Word frequency counter
- Log file organizer – auto-moves `.log` files into dated folders
- JSON serialization with `json.dump` / `json.load`

**Run:**
```bash
python task1_file_handling.py
```

---

## ✅ Task 2 – API Integration & JSON Handling

**APIs Used:** JSONPlaceholder, Open-Meteo (no API key needed)

**Features:**
- Fetch users, posts, comments via GET requests
- Query parameter filtering
- Full exception handling (ConnectionError, Timeout, HTTPError)
- Save API responses to local `.json` files

**Install & Run:**
```bash
pip install requests
python task2_api_integration.py
```

---

## ✅ Task 4 – Flask Mini Project: Student Contact Book

**Features:**
- Full CRUD (Create, Read, Update, Delete)
- Search by name, email, or department
- Bootstrap 5 responsive UI
- Flash messages for user feedback
- JSON file-based data storage

**Install & Run:**
```bash
cd flask_app
pip install flask
python app.py
# Open http://127.0.0.1:5000
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core language |
| `os`, `csv`, `json`, `shutil` | File handling |
| `requests` | API integration |
| `Flask` | Web framework |
| `Bootstrap 5` | Frontend UI |

---

*Submitted as part of the Alfido Tech Python Developer Internship Program.*
