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
            number = input(prompt)
            if number.lower() == "ex":
                print("Exiting the program.")
                exit(0)
            return float(number)
        except ValueError:
            print("Помилка: Введіть правильне число.")

def calculator():
    print("Калькулятор. Введіть 'ex' для завершення програми.")
    
    result = get_number("Введіть перше число: ")

    while True:
        print("\nОберіть операцію:\n"
              "'+' — додавання, '-' — віднімання, '*' — множення, '/' — ділення\n"
              "'!-' — віднімання (з перестановкою), '!/' — ділення (з перестановкою)\n"
              "'^' — піднесення до степеня, '!^' — піднесення до степеня (з перестановкою)\n"
              "'ex' — для виходу з програми")

        operation = input("Введіть операцію: ").lower()
        
        if operation == 'ex':
            print(f"Ваш поточний результат = {result}")
            print("Exiting the program.")
            exit(0)

        num = get_number("Введіть наступне число: ")

        try:
            if operation == '+':
                result = add(result, num)
            elif operation == '-':
                result = subtract(result, num)
            elif operation == '!-':
                result = subtract(num, result)
            elif operation == '*':
                result = multiply(result, num)
            elif operation == '/':
                result = divide(result, num)
            elif operation == '!/':
                result = divide(num, result)
            elif operation == '^':
                result **= num
            elif operation == '!^':
                result = num ** result
            else:
                print("Помилка: Неправильна операція.")
                continue

            print(f"\nВаш поточний результат = {result}")

        except ValueError as e:
            print(e)

calculator()

