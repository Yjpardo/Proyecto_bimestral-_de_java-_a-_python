print("Libreria y descuentos al comprar")

#Variables
descuento = 0
total = 0
subtototal = 0
nombre_cliente = input("Ingrese el nombre del cliente: ")

tipo_cli = int(input("Ingrese el tipo de cliente: "))

cant_libro = int(input("Ingrese la cantidad de libros comprados: "))

costo_libro = float(input("Ingrese el costo del libro: "))

#Condicionales
if tipo_cli == 1:
    descuento =0.30
    
if tipo_cli == 2:
    descuento = 0.20

if tipo_cli == 3:
    descuento = 0.10

if tipo_cli == 1:
    descuento = 0.30
else:
    if tipo_cli == 2:
        descuento =0.20
    else:
        if tipo_cli == 3:
            descuento = 0.10
        else:
            print("El cliente no tiene descuento")

if cant_libro > 5 and cant_libro <= 10:
    descuento = descuento + 0.04
else:
    if cant_libro > 10:
        descuento = descuento + 0.08

subtotal = cant_libro * costo_libro
total = subtotal - (subtotal * descuento)

print(f"El nombre del cliente es: {nombre_cliente}")
print("El subtotal a pagar es: ", subtotal)
print("El descuento es: ", descuento)
print("El total a pagar es: ", total)

print("El cliente ", nombre_cliente, " tiene que pagar un total de ", subtotal, " dolares, pero con un descuento de ", descuento)
print("Su neto a pagar es : ", total, " dolares")
