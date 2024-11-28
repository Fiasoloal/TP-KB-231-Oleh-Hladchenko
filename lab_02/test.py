import unittest
from io import StringIO
import sys
import os
import tempfile
import csv

from lab_02 import addNewElement, deleteElement, updateElement, loadFromCSV, saveToCSV, printAllList, list

class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8')
        self.test_filename = self.test_file.name
        self.test_file.close()

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_addNewElement(self):
        addNewElement()
        self.assertEqual(len(list), 1)  
        self.assertEqual(list[0]['name'], "Test Student")  

    def test_deleteElement(self):
        list.append({"name": "Test Student", "phone": "123456", "email": "test@example.com", "address": "123 Test St"})
        deleteElement()
        self.assertEqual(len(list), 0)  

    def test_updateElement(self):
        list.append({"name": "Test Student", "phone": "123456", "email": "test@example.com", "address": "123 Test St"})
        updateElement()
        self.assertEqual(list[0]["phone"], "654321")  

    def test_loadFromCSV(self):
        data = [
            {"name": "Bob", "phone": "123456789", "email": "bob@example.com", "address": "1 Main St"},
            {"name": "Alice", "phone": "987654321", "email": "alice@example.com", "address": "2 Main St"}
        ]

        with open(self.test_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            writer.writerows(data)

        loadFromCSV(self.test_filename)
        self.assertEqual(len(list), 2)  
        self.assertEqual(list[0]["name"], "Bob")  

    def test_saveToCSV(self):

        list.append({"name": "Charlie", "phone": "123123123", "email": "charlie@example.com", "address": "3 Main St"})
        saveToCSV(self.test_filename)

        with open(self.test_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  
            self.assertEqual(rows[0]["name"], "Charlie")  

    def test_printAllList(self):
        list.append({"name": "Test Student", "phone": "123456", "email": "test@example.com", "address": "123 Test St"})
        captured_output = StringIO()
        sys.stdout = captured_output
        printAllList()
        sys.stdout = sys.__stdout__  

        self.assertIn("Test Student", captured_output.getvalue()) 
if __name__ == '__main__':
    unittest.main()
