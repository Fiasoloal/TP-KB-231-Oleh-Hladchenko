import csv
import sys

# Ім'я файлу за замовчуванням
DEFAULT_FILENAME = "students_directory.csv"

# Список студентів
list = []

# Друк списку
def printAllList():
    if not list:
        print("The student list is empty.")
    else:
        for elem in list:
            print(f"Student name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}")
    return

# Додавання нового елемента
def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added.")
    return

# Видалення елемента
def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found.")
    else:
        del list[deletePosition]
        print("Element has been deleted.")
    return

# Оновлення елемента
def updateElement():
    name = input("Please enter the name of the student to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    
    if updatePosition == -1:
        print("Student not found.")
    else:
        new_name = input(f"Please enter new name (current: {list[updatePosition]['name']}): ") or list[updatePosition]["name"]
        new_phone = input(f"Please enter new phone (current: {list[updatePosition]['phone']}): ") or list[updatePosition]["phone"]
        new_email = input(f"Please enter new email (current: {list[updatePosition]['email']}): ") or list[updatePosition]["email"]
        new_address = input(f"Please enter new address (current: {list[updatePosition]['address']}): ") or list[updatePosition]["address"]

        if new_name != list[updatePosition]["name"]:
            old_item = list[updatePosition]
            del list[updatePosition]

            newItem = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            }

            insertPosition = 0
            for item in list:
                if new_name > item["name"]:
                    insertPosition += 1
                else:
                    break
            list.insert(insertPosition, newItem)
            print(f"Student {old_item['name']}'s details have been updated to {new_name}.")
        else:
            list[updatePosition]["phone"] = new_phone
            list[updatePosition]["email"] = new_email
            list[updatePosition]["address"] = new_address
            print(f"Student {name}'s details have been updated.")
    return

# Завантаження даних із CSV
def loadFromCSV(filename):
    global list
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            list = [row for row in reader]
        print(f"Data loaded successfully from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
        list = []
    except Exception as e:
        print(f"Error loading file: {e}")

# Збереження даних у CSV
def saveToCSV(filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list)
        print(f"Data saved successfully to {filename}.")
    except Exception as e:
        print(f"Error saving file: {e}")

# Меню
def main():
    # Завантаження даних із файлу
    filename = DEFAULT_FILENAME
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    loadFromCSV(filename)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated.")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted.")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed.")
                printAllList()
            case "X" | "x":
                saveToCSV(filename)
                print(f"Data saved to {filename}. Exiting...")
                break
            case _:
                print("Wrong choice.")

# Запуск програми
if __name__ == "__main__":
    main()
