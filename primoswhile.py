print("Numeros primos con ciclo while")

#Variables
cont = 1
cont2 = 1
divisor = 0
      
n = int(input("Ingrese el limite del numero a verififcar: "))

#While
while cont <= n:
    num= int(input("Ingrese el numeor a verificar: "))
    while cont2 <= num:
        if num %cont2 ==0:
            divisor = divisor +1
        cont2 = cont2 +1
        
    if divisor == 2:
        print(num, " es primo")
    else:
        print(num, " no es primo")

    cont2 = 1
    devisor = 0
    cont = cont + 1

 
