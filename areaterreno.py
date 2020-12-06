print("Area de un terreno")
"""calculo del area de un terreno
para ello se debe calcular las dos figuras que lo conforman"""

"""Entrada de datos"""
#calculo de area del triangulo
a_triangulo = float(input("Introduce la altura del triangulo: "))

#calcular el area del rectangulo
a_rectangulo = float(input("Introduce la altura del rectangulo: "))

b_rectangulo = float(input("Introduce la base del rectangulo: "))

"""procesos"""
#proceso del triangulo
AC = (a_triangulo * b_rectangulo) / 2
print("El area del triangulo es: ", AC)
#proceso del rectangulo
B = (b_rectangulo * a_rectangulo)
print("El area de rectangulo es: ", B)

""" Salida de datos """
#Area total del poligono
area = AC + B
print("El area total del terreno es la suma de las dos figuras ", area) 



