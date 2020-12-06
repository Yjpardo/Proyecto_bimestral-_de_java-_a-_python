print ("Programa para convertir las horas en formato de 24 a formato de 12 horas")

"""Simplemente debo hacer que el usario coloque las horas a convertir"""

#Declar e inicializar variables
h24 = 0
h12 = 0
m12 = 0
m24 = 0

# Ingreso de datos de entrada
h24 = int(input("Ingrese la hora en formato se 24 a transformar "))
m24 = int(input("Ingresse los minutos a transfomar "))

#Condiciones para ejecutar el calculo correspondiente
if ((h24 < 24) and (h24 > 0)):
    if((h24 >= 0) and (h24 <=24)) and ((m24 >= 0) and (m24 <= 60)):
        if m24 == 60:
           h24 = h24 + 1
           m24 = 0
        else:
            m12 = m24
        if h24 >= 12:
            if h24 == 12:
                h12 = h24
            else:
                h12 = h24 - 12
            periodo = "p.m"
        print ("El tiempo de " + h24 +" horas y " + m24 +" minutos, en formato de 24 horas")
        print ("Equivale a " + h12 + " horas y " + m12 +" minutos 'p.m'")
else:
    if h24 == 0:
        h12 = h24
        if m24 == 60:
            h12 = h12 + 1
            m24 = 0
        else:
            m12 = m24
        print ("El tiempo de " + h24 +" horas y " + m24 +" minutos, en formato de 24 horas")
        print ("Equivale a " + h12 + " horas y " + m12 +" minutos 'p.m'")
    else:
        if h24 == 24
        h12 = 0
            if m24 == 60
                h12 = h12 + 1
                m24 = 0
            else:
                m12 = m24
            print ("El tiempo de " + h24 +" horas y " + m24 +" minutos, en formato de 24 horas")
            print ("Equivale a " + h12 + " horas y " + m12 +" minutos 'p.m'")
print ("Fin")
