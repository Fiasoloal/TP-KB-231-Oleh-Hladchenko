def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Помилка: Ділення на нуль.")
    return x / y

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Помилка: Введіть правильне число.")

def calculator():
    print("Калькулятор. Введіть 'вихід' для завершення програми.")
    
    while True:
        num1 = get_number("Введіть перше число (або 'вихід' для завершення): ")
        operation = input("Введіть операцію (+, -, *, /): ")

        num2 = get_number("Введіть друге число: ")

        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Помилка: Неправильна операція.")
                continue

            print(f"Результат: {result}")

        except ValueError as e:
            print(e)

calculator()
