print("-------------------------------------")
print("Ejemplo de una factura con descuentos")
print("-------------------------------------")
"""Algoritmo con concionales que ayudan a
descubrrir el descuento d euna factura"""

#Variables
lim1 = 200
lim2 = 500
total = 0
descuento = 0

#Introducción de Variables
subtotal = int(input("ingrese el subtotal de su compra"))

#Condiciones
if ((subtotal >= lim1) and (subtotal < lim2)):
    descuento = 0.10;
else:
    if subtotal >= lim2:
        descuento = 0.15
if subtotal < lim1:
    print("No hay descuento por su compra por ser menor a 200 dolares")
    
total = subtotal - (subtotal * descuento)

print ("El total de la factura es: ", total)
print ("Fin")
