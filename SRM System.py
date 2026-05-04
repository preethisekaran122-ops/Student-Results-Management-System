import json
import os

DATA_FILE = "students.json"

# ── Load / Save ───────────────────────────────────────────────────────────────

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ── Grade Logic ───────────────────────────────────────────────────────────────

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "FAIL"

def get_marks(subject):
    while True:
        try:
            mark = int(input(f"  {subject}: "))
            if 0 <= mark <= 100:
                return mark
            print("  Please enter a value between 0 and 100.")
        except ValueError:
            print("  Invalid input. Enter a number.")

# ── Features ──────────────────────────────────────────────────────────────────

def add_student(data):
    print("\n--- Add Student ---")
    name = input("Student Name: ").strip().title()
    if name in data:
        print(f"Record for '{name}' already exists. Use Update option.")
        return

    roll = input("Roll Number: ").strip()
    subjects = ["Maths", "English", "Science", "Social", "Computer"]
    print("Enter marks (0-100) for each subject:")
    marks = {sub: get_marks(sub) for sub in subjects}

    total   = sum(marks.values())
    average = round(total / len(marks), 2)
    grade   = assign_grade(average)

    data[name] = {
        "roll_number": roll,
        "marks":       marks,
        "total":       total,
        "average":     average,
        "grade":       grade
    }
    save_data(data)
    print(f"\n✔ Record added — {name} | Total: {total} | Avg: {average} | Grade: {grade}")

def view_all(data):
    print("\n--- All Student Results ---")
    if not data:
        print("No records found.")
        return
    print(f"\n{'Name':<20} {'Roll No':<10} {'Total':<8} {'Average':<10} {'Grade'}")
    print("-" * 58)
    for name, info in sorted(data.items()):
        print(f"{name:<20} {info['roll_number']:<10} {info['total']:<8} {info['average']:<10} {info['grade']}")

def search_student(data):
    print("\n--- Search Student ---")
    name = input("Enter student name: ").strip().title()
    if name not in data:
        print(f"No record found for '{name}'.")
        return
    info = data[name]
    print(f"\nName        : {name}")
    print(f"Roll Number : {info['roll_number']}")
    print(f"{'Subject':<12} {'Marks'}")
    print("-" * 22)
    for sub, mark in info["marks"].items():
        print(f"  {sub:<12} {mark}")
    print("-" * 22)
    print(f"  {'Total':<12} {info['total']}")
    print(f"  {'Average':<12} {info['average']}")
    print(f"  {'Grade':<12} {info['grade']}")

def update_student(data):
    print("\n--- Update Student Marks ---")
    name = input("Enter student name to update: ").strip().title()
    if name not in data:
        print(f"No record found for '{name}'.")
        return
    subjects = list(data[name]["marks"].keys())
    print("Enter updated marks:")
    marks = {sub: get_marks(sub) for sub in subjects}

    total   = sum(marks.values())
    average = round(total / len(marks), 2)
    grade   = assign_grade(average)

    data[name]["marks"]   = marks
    data[name]["total"]   = total
    data[name]["average"] = average
    data[name]["grade"]   = grade
    save_data(data)
    print(f"✔ Record updated — {name} | Total: {total} | Avg: {average} | Grade: {grade}")

def delete_student(data):
    print("\n--- Delete Student Record ---")
    name = input("Enter student name to delete: ").strip().title()
    if name not in data:
        print(f"No record found for '{name}'.")
        return
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del data[name]
        save_data(data)
        print(f"✔ Record for '{name}' deleted.")
    else:
        print("Deletion cancelled.")

def class_summary(data):
    print("\n--- Class Summary ---")
    if not data:
        print("No records found.")
        return
    averages = [info["average"] for info in data.values()]
    totals   = [info["total"]   for info in data.values()]

    class_avg    = round(sum(averages) / len(averages), 2)
    topper_name  = max(data, key=lambda n: data[n]["average"])
    topper_avg   = data[topper_name]["average"]

    grade_counts = {}
    for info in data.values():
        g = info["grade"]
        grade_counts[g] = grade_counts.get(g, 0) + 1

    print(f"  Total Students  : {len(data)}")
    print(f"  Class Average   : {class_avg}%")
    print(f"  Highest Average : {topper_avg}% ({topper_name})")
    print(f"  Grade Distribution:")
    for grade, count in sorted(grade_counts.items()):
        print(f"    {grade}: {count} student(s)")

# ── Menu ──────────────────────────────────────────────────────────────────────

def main():
    data = load_data()
    menu = {
        "1": ("Add Student",          add_student),
        "2": ("View All Results",     view_all),
        "3": ("Search Student",       search_student),
        "4": ("Update Student Marks", update_student),
        "5": ("Delete Student",       delete_student),
        "6": ("Class Summary",        class_summary),
        "7": ("Exit",                 None),
    }

    print("=" * 45)
    print("   Student Result Management System")
    print("=" * 45)

    while True:
        print("\n--- Menu ---")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\nEnter choice: ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1](data)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
