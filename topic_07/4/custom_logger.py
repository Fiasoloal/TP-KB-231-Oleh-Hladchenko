import logging

class Logger:
    def __init__(self, filename="calculator.log"):
        logging.basicConfig(
            filename=filename,
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

    def log(self, a, b, operation, result):
        logging.info(f"Число 1: {a}, Число 2: {b}, Операція: {operation}, Результат: {result}")
