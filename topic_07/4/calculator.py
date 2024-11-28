from custom_logger import Logger
from functions import Operations
from operations import InputHandler


class Calculator:
    def __init__(self):
        self.logger = Logger()
        self.operations = Operations()
        self.input_handler = InputHandler()

    def log_operation(self, a, b, operation, result):
        self.logger.log_operation(a, b, operation, result)

    def calculation(self):
        a = self.input_handler.enter()
        while True:
            b = self.input_handler.enter()
            act = self.input_handler.actions(a)

            match act:
                case "+":
                    result = self.operations.sum(a, b)
                case "-":
                    result = self.operations.sub(a, b)
                case "!-":
                    result = self.operations.rsub(a, b)
                case "*":
                    result = self.operations.mult(a, b)
                case "/":
                    result = self.operations.div(a, b)
                case "!/":
                    result = self.operations.rdiv(a, b)
                case "^":
                    result = self.operations.deg(a, b)
                case "!^":
                    result = self.operations.rdeg(a, b)

            self.log_operation(a, b, act, result)
            a = result
            print("\nПоточний результат =", a)

if __name__ == "__main__":
    calc = Calculator()
    calc.calculation()
