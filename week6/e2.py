# Exercise 2: Student Grade Analyzer

# 1. Initialize Data Structures
# TODO: Create an empty dictionary to store student names and their grades.
#Keys will be student names (string), values will be lists of grades (integers or floats).
# Example:
student_grades = {
    "John": [85, 90, 95],
    "Jane": [80, 85, 90],
    "Jim": [75, 80, 85],
    "Jill": [70, 75, 80],
}

# 2. Function to Add Student Grades
# TODO: Define a function that prompts the user for a student's name and multiple grades.
#Store these grades in the student_grades dictionary.
#Handle cases where a student already exists or is new.
# def add_student_grades(grades_db):
## ... implementation ...
#pass

def add_student_grades(grades_db):
    student_name = input("Enter the student name: ")
    grades_input = input("Enter the grades: ")
    grades = grades_input.split(",")
    grades = [int(grade) for grade in grades]
    if student_name in grades_db:
        print("Student already exists, adding grades to existing student? (y/n)")
        if input() == "y":
            grades_db[student_name].extend(grades)
        else:
            print("Student not added")
    else:
        grades_db[student_name] = grades
        print("New student added")


# 3. Function to Calculate Statistics
# TODO: Define a function that takes a student's name and calculates their:
#- Average grade
#- Highest grade
#- Lowest grade
#Handle cases where the student is not found or has no grades.
# def get_student_stats(grades_db, student_name):
## ... implementation ...
#pass

def get_student_stats(grades_db, student_name):
    if student_name in grades_db:
        print(f"Student: {student_name}")
        print(f"Grades: {grades_db[student_name]}")
        print(f"Average grade: {sum(grades_db[student_name]) / len(grades_db[student_name])}")
        print(f"Highest grade: {max(grades_db[student_name])}")
        print(f"Lowest grade: {min(grades_db[student_name])}")
    else:
        print("Student not found")

# 4. Function to Generate Full Report
# TODO: Define a function that prints a report for all students, including their:
#- Name
#- All recorded grades
#- Average grade
#- Highest grade
#- Lowest grade
#Also, calculate and display the overall average grade for all students.
# def generate_full_report(grades_db):
## ... implementation ...
#pass

def generate_full_report(grades_db):
    for student_name in grades_db:
        print(f"Student: {student_name}")
        print(f"Grades: {grades_db[student_name]}")
        print(f"Average grade: {sum(grades_db[student_name]) / len(grades_db[student_name])}")
        print(f"Highest grade: {max(grades_db[student_name])}")
        print(f"Lowest grade: {min(grades_db[student_name])}")

    print(f"Overall average grade: {sum(grades_db[student_name]) / len(grades_db[student_name])}")

# 5. Main Program Loop
# TODO: Implement a loop that allows the user to:
#- Add grades for a student
#- View statistics for a specific student
#- Generate a full report for all students
#- Exit the program
# Example usage:
# while True:
#print("\nStudent Grade Analyzer Menu:")
#print("1. Add grades for a student")
#print("2. View statistics for a student")
#print("3. Generate full report")
#print("4. Exit")
#choice = input("Enter your choice: ")
#if choice == '1':
## ... call add_student_grades ...
#pass
#
#
#
#elif choice == '4':
#break
# ... other choices ...
while True:
    print("Menu:")
    print("1. Add grades for a student")
    print("2. View statistics for a student")
    print("3. Generate full report")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student_grades(student_grades)
    elif choice == '2':
        get_student_stats(student_grades, input("Enter the student name: "))   
    elif choice == '3':
        generate_full_report(student_grades)
    elif choice == '4':
        break
    else:
        print("Invalid choice")
    