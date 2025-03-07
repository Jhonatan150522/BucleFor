# Diseñe un pseudocódigo que lea el valor de un ángulo expresado en radianes y calcule e
# imprima el valor del seno de dicho ángulo. Se leerá también el número de términos de la serie.
# SEN(X) = X - ( X 3 / 3 ! ) + ( X 5 / 5 ! ) - (X7/ 7!) + .....

#Se importa math para poder realizar los calculos
import math

#Se le pide al usuario el valor del ángulo en radianes
x = float(input("Ingrese el valor del ángulo en radianes: "))

#Leer el número de términos de la serie
n = int(input("Ingrese el número de términos de la serie: "))

#Inicializar el valor del seno de x
seno = 0  

#Se calcula la serie de Taylor
for i in range(n):
    termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    seno += termino

#Se imprime todos los resultados
print(f"El valor aproximado de sen({x}) usando {n} términos es: {seno}")
