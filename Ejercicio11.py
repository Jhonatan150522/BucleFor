# Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y
# un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar
# es:
# Cn = C * (1 + x/100) ^ n
# Donde C es el capital inicial, x es la tasa de interés y n es el número de años a calcular.
# Solicitar entrada al usuario
C = float(input("Ingrese la cantidad de pesos inicial: "))
x = float(input("Ingrese la tasa de interés en porcentaje: "))
n = int(input("Ingrese el número de años: "))

if C > 0 and x >= 0 and n > 0:
    Cn = C * (1 + x / 100) ** n
    print(f"El monto final después de {n} años será: {Cn:.2f} pesos")
else:
    print("Por favor, ingrese valores válidos (capital positivo, tasa no negativa y años positivos).")
