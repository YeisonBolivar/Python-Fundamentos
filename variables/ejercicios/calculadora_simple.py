"""
Calculadora Simple
Declara dos variables numéricas (precio y cantidad). Calcula el total (precio × cantidad), aplica un 10% de descuento y muestra el resultado final.
"""

precio = 5
cantida = 2

total = precio * cantida

totalConDescuento = total - (total*0.1)

print(f"precio: {precio}")
print(f"cantidad: {cantida}")
print(f"total: {total}")
print(f"Total con descuento aplicado: {totalConDescuento}")

