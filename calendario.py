print("******************************")
print ("Calendario")

#Variables
año = int(input("Ingrese el año de nacimiento: "))
meses = int(input("Ingrese el mes de nacimiento: "))
dias = int(input("Ingrese el dia de nacimiento: "))
actual  =  2020
actual2 = 12
actual3 = 1

#Proceso
if año < actual:
    edad = actual - año
else:
        print("El año supera al año actual")

if meses <= 12:
    edad2 = actual2 - meses
else:
        print("El mes que coloco supera al limite de 12 mese")

if dias <= 31:
    edad3 = actual3 - dias
else:
    print("los dias colocados supera el limite de 31 dias")


print ("Usted tiene ", edad, " años, ", edad2, " meses y ", edad3, " dias")
