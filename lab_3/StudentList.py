from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.students.sort(key=lambda x: x.name)  
        
    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} has been deleted.")
                return
        print("Student not found.")

    def update_student(self, name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for student in self.students:
            if student.name == name:
                student.update(new_name, new_phone, new_email, new_address)
                print(f"Student {name}'s details have been updated.")
                return
        print("Student not found.")

    def print_all(self):
        if not self.students:
            print("The student list is empty.")
        else:
            for student in self.students:
                print(student)

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None
