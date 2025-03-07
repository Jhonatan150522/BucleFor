# En una empresa de 100 trabajadores, se hará un aumento al salario de acuerdo al tiempo de
# servicio, para este aumento se tomará en cuenta lo siguiente:\
# Se le pide al usuario la cantidad de trabajadores
num_trabajadores = int(input("Ingrese el número de trabajadores: "))

# Variables para contar cuántos trabajadores están en cada categoría y el total de aumentos
trabajadores_1_5 = 0
trabajadores_5_10 = 0
trabajadores_10_20 = 0
trabajadores_20_mas = 0

total_aumento_1_5 = 0
total_aumento_5_10 = 0
total_aumento_10_20 = 0
total_aumento_20_mas = 0

# Se recorre cada trabajador
for i in range(1, num_trabajadores + 1):
    años = int(input(f"Ingrese los años de servicio del trabajador {i}: "))

    # Se determina el aumento de salario según los años de servicio
    if 1 <= años < 5:
        aumento = 100
        trabajadores_1_5 += 1
        total_aumento_1_5 += aumento
    elif 5 <= años < 10:
        aumento = 250
        trabajadores_5_10 += 1
        total_aumento_5_10 += aumento
    elif 10 <= años < 20:
        aumento = 400
        trabajadores_10_20 += 1
        total_aumento_10_20 += aumento
    elif años >= 20:
        aumento = 550
        trabajadores_20_mas += 1
        total_aumento_20_mas += aumento
    else:
        aumento = 0  # Si el usuario ingresa 0 o un número negativo

    # Mostrar el aumento de cada trabajador
    if aumento > 0:
        print(f"El trabajador {i} con {años} años de servicio recibe un aumento de: {aumento} PESOS")
    else:
        print(f"El trabajador {i} no tiene derecho a un aumento o ingresó un valor inválido.")

# Se calcula el total de aumentos
total_general = total_aumento_1_5 + total_aumento_5_10 + total_aumento_10_20 + total_aumento_20_mas

# Se muestran los resultados finales
print("\nResumen de aumentos:")
print(f"Trabajadores con 1 a 5 años: {trabajadores_1_5} - Total aumento: {total_aumento_1_5} PESOS")
print(f"Trabajadores con 5 a 10 años: {trabajadores_5_10} - Total aumento: {total_aumento_5_10} PESOS")
print(f"Trabajadores con 10 a 20 años: {trabajadores_10_20} - Total aumento: {total_aumento_10_20} PESOS")
print(f"Trabajadores con más de 20 años: {trabajadores_20_mas} - Total aumento: {total_aumento_20_mas} PESOS")
print(f"\nTotal de aumentos para todos los trabajadores: {total_general} PESOS")
