"""
Intercambio de Variables (RETO)
Declara a = 5 y b = 10. Intercambia sus valores sin usar una tercera variable auxiliar. Muestra los valores antes y después. Pista: Python tiene una
forma elegante de hacerlo en una línea.

"""


a = 5
b = 10

print(f"a: {a}")
print(f"b: {b}")

a, b = b, a

print(f"a: {a}")
print(f"b: {b}")