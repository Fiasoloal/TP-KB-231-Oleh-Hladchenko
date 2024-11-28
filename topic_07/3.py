class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"

students = [
    Student("Vit", 21),
    Student("Di", 19),
    Student("Jonh", 22),
    Student("Frid", 20)
]

# Сортуємо список студентів за віком, використовуючи lambda функцію
sorted_students = sorted(students, key=lambda student: student.age)
print("\nСортування за віком:")
for student in sorted_students:
    print(student)

# Сортуємо список студентів за іменем, використовуючи lambda функцію
sorted_by_name = sorted(students, key=lambda student: student.name)
print("\nСортування за іменем:")
for student in sorted_by_name:
    print(student)