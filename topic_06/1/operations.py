# operations.py

def enter():
    while True:
        a = input("Для виходу з програми введіть 'ex' \nВведіть число: ")
        if a.lower() == "ex":
            exit(0)
        try:
            return float(a)
        except ValueError:
            print("Неправильний ввід. Будь ласка, введіть правильне число.")

def actions(a):
    print("\nКоманди:\n'+' — додати, '-' — відняти, '!-' — відняти навпаки, '*' — множити, '/' — ділити, '!/' — ділити навпаки, '^' — піднести до степеня, '!^' — піднести до степеня навпаки\nВведіть 'ex' для виходу.")
    action = input("Виберіть дію: ")
    if action == "ex":
        print("\nВаш поточний результат:", a)
        exit(0)
    elif action in ["+", "-", "!-", "*", "/", "!/", "^", "!^"]:
        return action
    else:
        print("Неправильна дія. Спробуйте ще раз.")
        return actions(a) 