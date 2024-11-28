# FileUtils.py
import csv
from Student import Student

class FileUtils:
    @staticmethod
    def load_from_csv(filename, student_list):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["phone"], row["email"], row["address"])
                    student_list.add_student(student)
            print(f"Data loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading file: {e}")

    @staticmethod
    def save_to_csv(filename, student_list):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                fieldnames = ["name", "phone", "email", "address"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "email": student.email,
                        "address": student.address
                    })
            print(f"Data saved successfully to {filename}.")
        except Exception as e:
            print(f"Error saving file: {e}")
