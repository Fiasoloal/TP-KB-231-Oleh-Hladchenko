#1)	Написати функцію пошуку коренів квадратного рівняння використовуючи функцію 
#розрахунку дискримінанту з попередньої теми та умовні переходи.

import math

def discriminant(a, b, c):
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Два корені: x1 = {root1}, x2 = {root2}"
    elif d == 0:
        root = -b / (2 * a)
        return f"Один корінь: x = {root}"
    else:
        return "Коренів немає"

a = 1  
b = -3  
c = 2  
print(find_roots(a, b, c))  
