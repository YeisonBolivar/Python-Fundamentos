"""
Calculadora de Descuentos (RETO)
Una tienda aplica descuentos: 20% si el total > 500, 10% si el total > 200, y 5% si es cliente VIP (usa una variable boolean). Calcula y muestra el precio
final considerando todas las condiciones.

"""
descuento = 0
total = 600
vip = True


if total > 500:
    descuento+= 0.2
elif total >200:
    descuento+= 0.1


if vip:
    descuento +=0.05

totalDescuento = total - (total*descuento)
print(f"Su compra es : {total}")
print(f"Su descuentos es de {descuento*100:.0f}%")
print(f"El precio final con descuento es: {totalDescuento:.0f}")
print(f"Lo que supone que tiene un ahorro en la compra de: {total*descuento:.0f}")


