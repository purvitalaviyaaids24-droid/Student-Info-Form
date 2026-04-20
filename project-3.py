import csv
import os

FILE_NAME = "students.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll No", "Math", "Science", "English", "Average"])


# Validate name
def validate_name(name):
    return name.replace(" ", "").isalpha()


# Validate marks
def validate_marks(marks):
    return 0 <= marks <= 100


# Check unique roll number
def is_unique_roll(roll):
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Roll No"] == str(roll):
                return False
    return True


# Add student
def add_student():
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name! Use only alphabets.")
        return

    roll = input("Enter roll number: ")
    if not roll.isdigit() or not is_unique_roll(roll):
        print("Invalid or duplicate roll number!")
        return

    try:
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))
        english = int(input("Enter English marks: "))

        if not (validate_marks(math) and validate_marks(science) and validate_marks(english)):
            print("Marks should be between 0 and 100.")
            return

    except ValueError:
        print("Enter valid numeric marks.")
        return

    avg = (math + science + english) / 3

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, math, science, english, round(avg, 2)])

    print("Student added successfully!")


# Display summary
def display_summary():
    students = []

    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    if not students:
        print("No data available.")
        return

    averages = [float(s["Average"]) for s in students]

    highest = max(students, key=lambda x: float(x["Average"]))
    lowest = min(students, key=lambda x: float(x["Average"]))

    print("\nSummary Report")
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {round(sum(averages)/len(averages), 2)}")

    print(f"\nTopper: {highest['Name']} (Avg: {highest['Average']})")
    print(f"Lowest: {lowest['Name']} (Avg: {lowest['Average']})")


# Menu
def menu():
    initialize_file()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    menu()

    