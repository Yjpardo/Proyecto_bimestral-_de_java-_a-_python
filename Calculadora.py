print("Calculadora básica con la estructura switch")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
print("Menu de operaciones")
print("Operaciones opcionales")
print("1. Suma")
print("2. Resta")
print("3. Mutlplicación")
print("4. División \n")
opcion = int(input("Cual es tu opción deseada: "))

#Operación
def Suma(x, y): 
    return x + y
def Resta(x, y):
    return x - y
def Multiplicacion(x, y):
    return x * y
def Division(x, y):
    return x / y

if opcion == 1:
    print(n1, "+", n2, " = ", Suma(n1, n2))
    
elif opcion == 2:
    print(n1, "-", n2, " = ", Resta(n1, n2))

elif opcion == 3:
    print(n1, "*", n2, " = ", Multiplicacion(n1, n2))
    
elif opcion == 4:
    print(n1, "/" , n2, " = ", Division(n1, n2))

else:
    print("opcion invalida")
