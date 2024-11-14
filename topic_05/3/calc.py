# calc.py

from operations import enter, actions
from functions import sum, sub, rsub, mult, div, rdiv, deg, rdeg

def calculation():
    a = enter()
    while True:
        b = enter()
        act = actions(a)

        match act:
            case "+":
                a = sum(a, b)
            case "-":
                a = sub(a, b)
            case "!-":
                a = rsub(a, b)
            case "*":
                a = mult(a, b)
            case "/":
                a = div(a, b)
            case "!/":
                a = rdiv(a, b)
            case "^":
                a = deg(a, b)
            case "!^":
                a = rdeg(a, b)

        print("\nПоточний результат =", a)

# Запуск калькулятора
calculation()
