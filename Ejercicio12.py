# Generar un algoritmo que permita realizar las siguientes conversiones de un número entero a
# octal y hexadecimal. En la siguiente tabla, encontrar las equivalencias de los valores entre los
# sistemas decimal, binario, octal y hexadecimal.
# Solicitar entrada al usuario
num = int(input("Ingrese un número entero: "))

if num >= 0:
    octal = oct(num)[2:]  # Convertir a octal y quitar prefijo '0o'
    hexadecimal = hex(num)[2:].upper()  # Convertir a hexadecimal y quitar prefijo '0x'
    
    print(f"El número {num} en octal es: {octal}")
    print(f"El número {num} en hexadecimal es: {hexadecimal}")
else:
    print("Por favor, ingrese un número entero positivo o cero.")
