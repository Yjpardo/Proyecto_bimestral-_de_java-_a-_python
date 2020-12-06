print("identificar el mayor de tres numeros")
"""ALgoritmo que ayuda a encontre el de mayor
colocando tres variables del tipo entero"""

#Introducción de variables
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

#Condiciones
if num1 > num2:
    if num1 > num3:
        print("El mayor es: ", num1)
    else:
        print("El mayor es :", num3)
    
elif num2 > num3:
    print("El mayor es: ", num2)
else:
    print("El mayor es: ",num3)

print("==========================")
print("Fin")
Print("==========================")
