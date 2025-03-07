# Hacer un algoritmo que al ingresar N números por la pantalla y se calcule la suma, resta,
# multiplicación y división. El proceso debe terminar cuando se hallan realizado 10 procesos
# (Hacer uso de contadores).
# Inicializar contadores de operaciones
contador_suma = 0
contador_resta = 0
contador_multiplicacion = 0
contador_division = 0

# Realizar 10 procesos con for
for i in range(10):
    num1 = float(input(f"Proceso {i + 1}: Ingrese el primer número: "))
    num2 = float(input(f"Proceso {i + 1}: Ingrese el segundo número: "))
    
    # Realizar operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "Indefinido (División por cero)"

    # Aumentar contadores
    contador_suma += 1
    contador_resta += 1
    contador_multiplicacion += 1
    if num2 != 0:
        contador_division += 1  # Solo contar si no hay división por 0

    # Mostrar resultados
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# Mostrar el resumen de operaciones realizadas
print("\nResumen de operaciones realizadas:")
print(f"Suma realizada {contador_suma} veces.")
print(f"Resta realizada {contador_resta} veces.")
print(f"Multiplicación realizada {contador_multiplicacion} veces.")
print(f"División realizada {contador_division} veces (sin contar divisiones por 0).")
print("Se han realizado 10 procesos. Fin del programa.")
