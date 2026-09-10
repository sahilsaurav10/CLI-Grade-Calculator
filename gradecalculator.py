def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_percentage(marks):
    total = sum(marks.values())
    maximum = len(marks) * 100
    return (total / maximum) * 100


def display_result(student):
    percentage = calculate_percentage(student["marks"])
    grade = calculate_grade(percentage)

    print("\n========== RESULT ==========")
    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("\nSubject Marks:")

    for subject, marks in student["marks"].items():
        print(subject, ":", marks)

    print("\nTotal:", sum(student["marks"].values()), "/", len(student["marks"]) * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    if grade == "F":
        print("Status: Fail")
    else:
        print("Status: Pass")

    print("============================")


def main():
    print("===== CLI GRADE CALCULATOR =====")

    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        subjects = {}
        number_of_subjects = int(input("Enter number of subjects: "))

        for j in range(number_of_subjects):
            subject = input("Enter subject name: ")
            marks = float(input("Enter marks out of 100: "))

            while marks < 0 or marks > 100:
                print("Invalid marks. Enter marks between 0 and 100.")
                marks = float(input("Enter marks out of 100: "))

            subjects[subject] = marks

        students[roll] = {
            "name": name,
            "roll": roll,
            "marks": subjects
        }

    while True:
        print("\n===== MENU =====")
        print("1. View All Students")
        print("2. Search Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(students) == 0:
                print("No student records found.")
            else:
                for student in students.values():
                    display_result(student)

        elif choice == "2":
            roll = input("Enter roll number: ")

            if roll in students:
                display_result(students[roll])
            else:
                print("Student not found.")

        elif choice == "3":
            print("Thank you for using CLI Grade Calculator!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
