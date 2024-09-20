# Написати функцію пошуку дискримінанту квадратного рівняння.

def find_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

a, b, c = 1, -3, 2
d = find_discriminant(a, b, c)
print(f"Дискримінант: {d}") 
