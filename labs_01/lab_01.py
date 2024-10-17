# Додано нові поля: email і address для кожного студента
# Додано функцію updateElement, яка дозволяє оновлювати існуючі записи студента
# Додано можливість пропуску полів при оновленні (зберігає старі дані, якщо нові не введено)

# уже відсортований список із 4 полями: ім’я, телефон, електронна адреса, адреса
list = [
    {"name": "Bob", "phone": "0631234567", "email": "bobisingers@example.com", "address": "123 Main St"},
    {"name": "Emma", "phone": "0631234568", "email": "emma2004@example.com", "address": "456 Park Ave"},
    {"name": "Jon",  "phone": "0631234569", "email": "jonyStre@example.com", "address": "789 Elm St"},
    {"name": "Zak",  "phone": "0631234570", "email": "ZakKing@example.com", "address": "101 Oak St"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}"
        print(strForPrint)
    return

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
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter the name of the student to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    
    if updatePosition == -1:
        print("Student not found")
    else:
# Дозволяє користувачу оновлювати кожне поле або залишити його без змін
        new_phone = input(f"Please enter new phone (current: {list[updatePosition]['phone']}): ") or list[updatePosition]["phone"]
        new_email = input(f"Please enter new email (current: {list[updatePosition]['email']}): ") or list[updatePosition]["email"]
        new_address = input(f"Please enter new address (current: {list[updatePosition]['address']}): ") or list[updatePosition]["address"]
        
# Оновлення інформації про студента
        list[updatePosition]["phone"] = new_phone
        list[updatePosition]["email"] = new_email
        list[updatePosition]["address"] = new_address
        
        print(f"Student {name}'s details have been updated.")
# Пересортований список
        list.sort(key=lambda x: x["name"])
    return
# Меню
def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exiting...")
                break
            case _:
                print("Wrong choice")

main()
