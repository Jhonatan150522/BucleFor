# Construya los algoritmos que permitan calcular las siguientes series con un valor de N
# ingresado desde teclado:
# Solicitar entrada al usuario
N = int(input("Ingrese un número positivo N: "))
# Se le agragra la condicional if
if N > 0:
    suma_cuadrados = 0
    suma_potencias = 0
    
    for i in range(1, N+1):
        suma_cuadrados += i**2
        suma_potencias += i**i
    
    print(f"Resultado de la primera serie (sumatoria de cuadrados): {suma_cuadrados}")
    print(f"Resultado de la segunda serie (sumatoria de potencias): {suma_potencias}")
else:
    print("Por favor, ingrese un número positivo.")
