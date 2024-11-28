class Operations:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def rsub(a, b):
        return b - a

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            return "Cannot divide by 0. Please enter a different number."
        return a / b

    @staticmethod
    def rdiv(a, b):
        if a == 0:
            return "Cannot divide by 0. Result is 0. Try another action."
        return b / a

    @staticmethod
    def deg(a, b):
        return a ** b

    @staticmethod
    def rdeg(a, b):
        return b ** a
