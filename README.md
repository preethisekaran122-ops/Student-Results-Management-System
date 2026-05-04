# Student Result Management System 🎓

A menu-driven command-line application built in Python to manage student academic records. Supports adding, viewing, searching, updating, and deleting student data with persistent JSON-based storage.

---

## Features

- **Add Student** — Enter marks for 5 subjects with input validation
- **View All Results** — Displays all student records in a formatted table
- **Search Student** — Look up a specific student's subject-wise marks and grade
- **Update Marks** — Edit an existing student's marks and recalculate results
- **Delete Record** — Remove a student entry with confirmation prompt
- **Class Summary** — Shows total students, class average, top performer, and grade distribution
- **Data Persistence** — All records are saved to a local `students.json` file

---

## Grade Scale

| Average (%)  | Grade |
|-------------|-------|
| 90 and above | A+    |
| 80 – 89      | A     |
| 70 – 79      | B     |
| 60 – 69      | C     |
| 50 – 59      | D     |
| Below 50     | FAIL  |

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python Student_Result_Management_System.py
```

---

## Sample Output

```
=============================================
   Student Result Management System
=============================================

--- Menu ---
  1. Add Student
  2. View All Results
  3. Search Student
  4. Update Student Marks
  5. Delete Student
  6. Class Summary
  7. Exit

--- All Student Results ---

Name                 Roll No    Total    Average    Grade
----------------------------------------------------------
Preethi              101        450      90.0       A+
Arun                 102        380      76.0       B

--- Class Summary ---
  Total Students  : 2
  Class Average   : 83.0%
  Highest Average : 90.0% (Preethi)
  Grade Distribution:
    A+: 1 student(s)
    B : 1 student(s)
```

---

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON (file-based persistence)
- **Concepts used:** Dictionaries, File I/O, Functions, Loops, Input Validation, Conditional Logic

---

## Author

**S. Preethi**  
M.Sc. Mathematics — Thiagarajar College, Madurai  
[LinkedIn](https://www.linkedin.com/in/preethi-sekaran-113019313) | [GitHub](https://github.com/preethisekaran122-ops/Student-Results-Management-System)
