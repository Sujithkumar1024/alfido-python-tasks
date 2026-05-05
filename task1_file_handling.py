"""
Task 1: Python File Handling & Automation
==========================================
Demonstrates:
- Reading and writing text/CSV files
- Exception handling
- Automating log file organization
- File search and word frequency analysis
"""

import os
import csv
import json
import shutil
from datetime import datetime


# ──────────────────────────────────────────
# 1. Write & Read a Text File
# ──────────────────────────────────────────
def write_text_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"[OK] Written to {filename}")
    except IOError as e:
        print(f"[ERROR] Writing file: {e}")

def read_text_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return None


# ──────────────────────────────────────────
# 2. CSV Handling
# ──────────────────────────────────────────
def create_sample_csv(filename):
    data = [
        ["Name", "Age", "City"],
        ["Alice", 28, "New York"],
        ["Bob", 34, "London"],
        ["Charlie", 22, "Mumbai"],
        ["Diana", 30, "Toronto"],
    ]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"[OK] CSV created: {filename}")

def read_csv_and_display(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            print(f"\n--- Contents of {filename} ---")
            for row in reader:
                print(f"  Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}")
    except FileNotFoundError:
        print(f"[ERROR] CSV not found: {filename}")


# ──────────────────────────────────────────
# 3. Word Frequency Counter
# ──────────────────────────────────────────
def word_frequency(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read().lower()
        words = text.split()
        freq = {}
        for word in words:
            word = word.strip('.,!?";:')
            freq[word] = freq.get(word, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(f"\n--- Top 5 words in {filename} ---")
        for word, count in sorted_freq[:5]:
            print(f"  '{word}': {count} time(s)")
        return freq
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return {}


# ──────────────────────────────────────────
# 4. Log File Organizer (Automation)
# ──────────────────────────────────────────
def organize_logs(source_dir, dest_dir):
    """Move .log files into dated folders."""
    os.makedirs(dest_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    target = os.path.join(dest_dir, today)
    os.makedirs(target, exist_ok=True)

    moved = 0
    for fname in os.listdir(source_dir):
        if fname.endswith('.log'):
            src = os.path.join(source_dir, fname)
            dst = os.path.join(target, fname)
            shutil.move(src, dst)
            moved += 1
    print(f"[OK] Moved {moved} log file(s) to {target}")


# ──────────────────────────────────────────
# 5. JSON Save & Load
# ──────────────────────────────────────────
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"[OK] JSON saved: {filename}")

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[ERROR] {e}")
        return None


# ──────────────────────────────────────────
# MAIN DEMO
# ──────────────────────────────────────────
if __name__ == "__main__":
    os.makedirs("demo_files", exist_ok=True)
    os.chdir("demo_files")

    # 1. Text file
    sample_text = "Python is powerful. Python makes automation easy. File handling in Python is simple and effective."
    write_text_file("sample.txt", sample_text)
    content = read_text_file("sample.txt")
    print(f"\nFile content:\n  {content}")

    # 2. Word frequency
    word_frequency("sample.txt")

    # 3. CSV
    create_sample_csv("people.csv")
    read_csv_and_display("people.csv")

    # 4. Log organizer
    os.makedirs("logs_raw", exist_ok=True)
    for i in range(3):
        with open(f"logs_raw/app_{i}.log", 'w') as f:
            f.write(f"Log entry {i}: {datetime.now()}\n")
    organize_logs("logs_raw", "logs_sorted")

    # 5. JSON
    user_data = {"name": "Intern", "task": "File Handling", "score": 100}
    save_json(user_data, "data.json")
    loaded = load_json("data.json")
    print(f"\nLoaded JSON: {loaded}")

    print("\n✅ Task 1 Complete!")
