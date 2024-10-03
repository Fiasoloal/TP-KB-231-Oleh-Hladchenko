#3)	Написати програму калькулятор використовуючи match конструкцію. 
#Кожна операція має бути виконана в окремій функції.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: не можна ділити на нуль!"
    return a / b

def calculator():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    operation = input("Введіть операцію (+, -, *, /): ")

    match operation:
        case '+':
            print(f"Результат: {add(a, b)}")
        case '-':
            print(f"Результат: {subtract(a, b)}")
        case '*':
            print(f"Результат: {multiply(a, b)}")
        case '/':
            print(f"Результат: {divide(a, b)}")
        case _:
            print("Помилка: невідома операція")

calculator()
