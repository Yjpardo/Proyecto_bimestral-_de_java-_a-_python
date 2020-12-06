print("================================")
print("Conversioncion de temperatura")
print("================================")

""" ALgoritmo que facilitara las conversion
de un tipo de temperatura a otro, pero en esta ocasion solo haré
de Celsius a Farenheit y Celsius a Kelvin""""

#Intoducción  de variables

C = float(input("Ingrese los grados Celsius"))

#Proceso
if gC > 0:
    gF = C * 9/5  + 32
        print ("La equivalencia en grados Farenheit es: ", gF)
    gK = gC * 273.14
        print ("La equivalencia en grados Kelvin es: ", gK)
print("Fin")
