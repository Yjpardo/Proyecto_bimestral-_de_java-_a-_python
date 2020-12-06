print("potencias")

#Variables
import math
cont = 0
resul = 0
base = int(input("Ingrese la base de la potencia: "))

pot = int(input("Ingrese la potencia: "))

#Condicionales
while cont <= pot:
    resul = resul * base
    cont = cont + 1

resul = (pow(base, pot))
print("la potencia de: ", base," elevado a ", pot," es: ", resul) 
