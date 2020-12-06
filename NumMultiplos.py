print("Un numero y multiplos")

#Variables
cuadrado = 0
mitad = 0
num = int(input("Ingrese el numero a verificar: "))

#Condicionales
if num <= 100:
    if num% 4 == 0:
        mitad = num/2
    else:
        if num % 5 == 0:
            cuadrado = pow(num,2)
        else:
            if num % 6 == 0:
                num = num

print("La mitad del numero es: ", mitad)
print("El cuadrado del numero es: ", cuadrado)
print("El numero es: ", num)
