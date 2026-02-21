# Condicionales con logica combinada

hora = 14
llueve = True

if hora >= 12 and not llueve:
    print("!Hora de salir!")
elif llueve:
    print("Mejor lleva paraguas")
else:
    print("Espera un poco más")


# Condicional en una sola linea

edad = 19

msg = "Mayor" if edad >= 18 else "Menor"

print(f"Usted es {msg} de edad.")