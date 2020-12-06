print("Area de un poligono compuesto")
"""calculo del area de un poligono conpuesto
para ello se debe calcular las figuras que los conforman"""

"""Entrada de datos"""
#calcular del area del cuadrado
l_cuadrado = float(input("Ingrese el lado de cuadrado: "))

#calculo de 3 triangulos del mismo tamaño
a_triangulo = float(input("Introduce la altura del triangulo: "))

#calcular el area del rectangulo
a_rectangulo = float(input("Introduce la altura del rectangulo: "))

"""procesos"""
#proceso del cuadrado
A = l_cuadrado * l_cuadrado
print("El area del cuadrado es: ", A)
#proceso de los triangulos
B = (l_cuadrado * a_triangulo) / 2
ats = B * 3
print("El area de los 3 triangulos es: ", ats)
#proceso del rectangulo
D = (l_cuadrado * a_rectangulo)
print("El area de rectangulo es: ", D)

""" Salida de datos """
#Area total del poligono
area = A + ats + D
print("El area total de poligono compuesto es la suma de las anteriores figuras ", area) 


