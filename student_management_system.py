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