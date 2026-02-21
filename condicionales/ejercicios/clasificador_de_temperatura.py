"""
Clasificador de Temperaturas
Dada una temperatura, clasifícala como: Frío (< 10°C), Fresco (10-19°C), Agradable (20-25°C), Caluroso (26-35°C) o Extremo (> 35°C).

"""

temp = float(input("Digite la temperatura: "))



if temp > 35:
    msg = "Extremo"
elif temp >=26:
    msg = "Caluroso"
elif temp >=20:
    msg = "Agradable"
elif temp >=10:
    msg = "Fresco"
else:
    msg = "Frio"


print(f"La temperatura de {temp} es considerado {msg}")