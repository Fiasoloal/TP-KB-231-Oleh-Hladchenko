import unittest
from Student import Student
from StudentList import StudentList
from FileUtils import FileUtils
import os
from io import StringIO
import sys

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.phone, "1234567890")
        self.assertEqual(student.email, "johndoe@example.com")
        self.assertEqual(student.address, "123 Main St")

    def test_student_update(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        student.update(name="Jane Doe", phone="0987654321", email="janedoe@example.com", address="456 Main St")
        self.assertEqual(student.name, "Jane Doe")
        self.assertEqual(student.phone, "0987654321")
        self.assertEqual(student.email, "janedoe@example.com")
        self.assertEqual(student.address, "456 Main St")

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        self.student_list.add_student(student)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "John Doe")

    def test_delete_student(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        self.student_list.add_student(student)
        self.student_list.delete_student("John Doe")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        self.student_list.add_student(student)
        self.student_list.update_student("John Doe", new_name="Jane Doe", new_phone="0987654321")
        updated_student = self.student_list.find_student("Jane Doe")
        self.assertIsNotNone(updated_student)
        self.assertEqual(updated_student.name, "Jane Doe")
        self.assertEqual(updated_student.phone, "0987654321")

    def test_print_all(self):
        student = Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
        self.student_list.add_student(student)
        captured_output = StringIO()
        sys.stdout = captured_output
        self.student_list.print_all()
        sys.stdout = sys.__stdout__
        self.assertIn("John Doe", captured_output.getvalue())

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_students.csv"
        self.student_list = StudentList()
        self.student_list.add_student(Student("John Doe", "1234567890", "johndoe@example.com", "123 Main St"))

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_to_csv(self):
        FileUtils.save_to_csv(self.test_file, self.student_list)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_from_csv(self):
        FileUtils.save_to_csv(self.test_file, self.student_list)
        new_student_list = StudentList()
        FileUtils.load_from_csv(self.test_file, new_student_list)
        self.assertEqual(len(new_student_list.students), 1)
        self.assertEqual(new_student_list.students[0].name, "John Doe")

if __name__ == "__main__":
    unittest.main()
