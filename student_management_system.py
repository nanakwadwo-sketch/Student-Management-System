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