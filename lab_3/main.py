# main.py
from StudentList import StudentList
from FileUtils import FileUtils
from Student import Student  # Додаємо цей імпорт

def main():
    student_list = StudentList()

    # Завантаження даних із файлу
    filename = "students_directory.csv"
    FileUtils.load_from_csv(filename, student_list)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ").lower()
        if choice == "c":
            name = input("Please enter student name: ")
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            address = input("Please enter student address: ")
            student = Student(name, phone, email, address)
            student_list.add_student(student)
            print("New student added.")
        elif choice == "u":
            name = input("Enter the student's name to update: ")
            new_name = input(f"Enter new name (current: {name}): ") or None
            new_phone = input(f"Enter new phone (current: {name}): ") or None
            new_email = input(f"Enter new email (current: {name}): ") or None
            new_address = input(f"Enter new address (current: {name}): ") or None
            student_list.update_student(name, new_name, new_phone, new_email, new_address)
        elif choice == "d":
            name = input("Enter the student's name to delete: ")
            student_list.delete_student(name)
        elif choice == "p":
            student_list.print_all()
        elif choice == "x":
            FileUtils.save_to_csv(filename, student_list)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
