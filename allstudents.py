# Student Management System using Functions in Python

students = []

# Add student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    
    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")


# View all students
def view_students():
    if not students:
        print("No student records found.\n")
        return
    
    print("\nStudent Records:")
    print("-" * 30)
    for student in students:
        print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
    print()


# Search student by roll number
def search_student():
    roll_no = input("Enter roll number to search: ")
    
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}")
            print(f"Marks: {student['marks']}\n")
            return
    
    print("Student not found.\n")


# Update student details
def update_student():
    roll_no = input("Enter roll number to update: ")
    
    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ")
            student["marks"] = float(input("Enter new marks: "))
            print("Student record updated successfully!\n")
            return
    
    print("Student not found.\n")


# Delete student
def delete_student():
    roll_no = input("Enter roll number to delete: ")
    
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    
    print("Student not found.\n")


# Main menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program
menu()