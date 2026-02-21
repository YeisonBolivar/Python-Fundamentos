"""
Detector de Par o Impar
Pide al usuario un número con input(). Determina si es par o impar. Muestra un mensaje claro en cada caso. Pista: usa el operador módulo (%).

"""


n = int(input("Digite un numero: "))

print(f"el numero {n} es {"par" if n % 2 == 0 else "impar"}")