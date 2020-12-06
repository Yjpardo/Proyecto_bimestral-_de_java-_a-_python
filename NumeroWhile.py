print("Verificar un numero con un ciclo while")

#Variables
cont = 1
sumPar = 0
sumImpar = 0
sumPos = 0
sumNeg = 0

n = int(input("Ingrese el limite del ciclo a verificar: "))

#Condicionales
while cont <= n:
    num = int(input("Ingrese el numero a verificar: "))

    if num % 2 == 0:
        sumPar = sumPar + num
    else:
        sumImpar = sumImpar + num

    if num > 0:
        sumPos = sumPos + num
    else:
        sumNeg = sumNeg + num
    cont = cont +1

print("La suma de los pares es: ", sumPar)
print("La suma de los impares es: ", sumImpar)
print("La suma de los positivos es: ", sumPos)
print("la suma de los negativos es: ", sumNeg)
