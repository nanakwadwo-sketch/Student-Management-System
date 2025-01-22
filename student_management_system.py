students ={}

def display_menu():
    
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. View Unique Courses")
    print("7. Exit")

#function to add students:
def add_student():
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id in students:
            print("Student ID already exists.")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        courses = input("Enter Courses (comma-separated): ").split(',')
        students[student_id] = {"name": name, "age": age, "courses": [course.strip() for course in courses]}
        print("Student added successfully.")
    except ValueError:
        print("Invalid input. Please try again.")

def update_student():
    try:
        student_id = int(input("Enter Student ID to update: "))
        if student_id not in students:
            print("Student ID not found.")
            return
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Courses")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            students[student_id]["name"] = input("Enter new name: ")
        elif choice == 2:
            students[student_id]["age"] = int(input("Enter new age: "))
        elif choice == 3:
            courses = input("Enter new courses (comma-separated): ").split(',')
            students[student_id]["courses"] = [course.strip() for course in courses]
        else:
            print("Invalid choice.")
            return
        print("Student updated successfully.")
    except ValueError:
        print("Invalid input. Please try again.")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n{:<10} {:<20} {:<5} {:<30}".format("ID", "Name", "Age", "Courses"))#display in a table format
    print("-" * 70)
    for student_id, details in students.items():
        print("{:<10} {:<20} {:<5} {:<30}".format(student_id, details["name"], details["age"], ', '.join(details["courses"])))

        #function to delete student records by id
def delete_student():
    try:
        student_id = int(input("Enter Student ID to delete: "))
        if student_id in students:
            del students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")
    except ValueError:
        print("Invalid input. Please try again.")

def search_student():
    try:
        student_id = int(input("Enter Student ID to search: "))
        if student_id in students:
            details = students[student_id]
            print("\nID: ", student_id)
            print("Name: ", details["name"])
            print("Age: ", details["age"])
            print("Courses: ", ', '.join(details["courses"]))
        else:
            print("Student ID not found.")
    except ValueError:
        print("Invalid input. Please try again.")
