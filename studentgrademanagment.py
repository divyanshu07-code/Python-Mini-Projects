# Student Grade Management System


students = {}

while True:
    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====") 
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - View Students")
    print("5 - Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        students[name] = grade
        print("Student added successfully!")

    # Update Student
    elif choice == "2":
        name = input("Enter student name to update: ")

        if name in students:
            marks = int(input("Enter new marks: "))

            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 50:
                grade = "C"
            else:
                grade = "Fail"

            students[name] = grade
            print("Student updated successfully!")

        else:
            print("Student not found!")

    # Delete Student
    elif choice == "3":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")

        else:
            print("Student not found!")

    # View Students
    elif choice == "4":
        print("\nStudent Records")

        if len(students) == 0:
            print("No records found!")

        else:
            for name, grade in students.items():
                print(name, ":", grade)

    # Exit
    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
