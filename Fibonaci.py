print("Ciclo For con la serie de Fibonaci")

#Variables
def fibo (n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo (n-2) + fibo (n-1)
    
num = int(input("Ingrese el limite de la serie fibonaci: "))
if num < 0:
    print ("Numero no valido")

i = 0

for i in range(0, num):
    print(fibo(i))
    
