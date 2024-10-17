def calculator():
    print("Калькулятор. Введіть 'вихід', щоб завершити програму.")
    while True:
        num1 = input("Введіть перше число (або 'вихід' для завершення): ")
        if num1.lower() == 'вихід':
            break
        num2 = input("Введіть друге число: ")
        operation = input("Введіть операцію (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                print("Неправильна операція.")
                continue

            print(f"Результат: {result}")
        except ValueError:
            print("Будь ласка, введіть правильні числа.")

calculator()
