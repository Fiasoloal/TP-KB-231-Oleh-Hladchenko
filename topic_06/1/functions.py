# functions.py

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def rsub(a, b):
    return b - a

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by 0. Please enter a different number."
    return a / b

def rdiv(a, b):
    if a == 0:
        return "Cannot divide by 0. Result is 0. Try another action."
    return b / a

def deg(a, b):
    return a ** b

def rdeg(a, b):
    return b ** a