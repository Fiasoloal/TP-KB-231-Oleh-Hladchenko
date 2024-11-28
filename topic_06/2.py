students = [
    {"ім'я": "Олексій", "оцінка": 85},
    {"ім'я": "Марія", "оцінка": 92},
    {"ім'я": "Іван", "оцінка": 78},
    {"ім'я": "Анна", "оцінка": 88}
]

# Сортування за іменем
sortedname = sorted(students, key=lambda x: x["ім'я"])
print("Сортування за іменем:")
print(sortedname)

# Сортування за оцінкою
sortedscore = sorted(students, key=lambda x: x["оцінка"])
print("Сортування за оцінкою:")
print(sortedscore)
