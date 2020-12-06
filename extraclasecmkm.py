print("Tarea extraclase sobre conversiones de medidas de longitud")
"""Constuye un programa que permita la conversion de  medidas de longitud
        Medidas de longitud 
        1 metro = 100 centrimetros
        1 kilometro = 1000 metros
        1 metro = 39,3701 pulgadas
        1 metro = 3,28084 pies"""
#metros a centimetros
m = float(input("Ingrese los metros para convertir en cm: "))

#metros a kilometros
m2 = float(input("Ingrese los metros para convertir en kilometros: "))

#metros a pies
m3 = float(input("Ingrese los metros para convertir en pies: "))
#metros a pulgadas
m4 = float(input("Ingrese los metros para convertir en pulgadas: "))

"""proceso"""
cm = m * 100
km = m2 / 1000
ft = m3 * 2.8084
ins = m4 * 39.3701

"""salida de datos"""
print("Total de centrimetros: ", cm)
print("Total de kilometros: ", km)
print("Total de pies: ", ft)
print("Total de pulgadas: ", ins)
