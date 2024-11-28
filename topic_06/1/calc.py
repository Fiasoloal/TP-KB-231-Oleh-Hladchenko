import logging
from operations import enter, actions
from functions import sum, sub, rsub, mult, div, rdiv, deg, rdeg

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_operation(a, b, operation, result):

    logging.info(f"Число 1: {a}, Число 2: {b}, Операція: {operation}, Результат: {result}")

def calculation():
    a = enter()
    while True:
        b = enter()
        act = actions(a)
        
        match act:
            case "+":
                result = sum(a, b)
            case "-":
                result = sub(a, b)
            case "!-":
                result = rsub(a, b)
            case "*":
                result = mult(a, b)
            case "/":
                result = div(a, b)
            case "!/":
                result = rdiv(a, b)
            case "^":
                result = deg(a, b)
            case "!^":
                result = rdeg(a, b)


        log_operation(a, b, act, result)
        a = result
        print("\nПоточний результат =", a)

calculation()
