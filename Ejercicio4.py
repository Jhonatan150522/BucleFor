#Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10, el segundo
#$20, el tercero $40 y así sucesivamente. Realice un algoritmo para determinar cuánto debe
#pagar mensualmente y el total de lo que pagó después de los 20 meses y represéntelo
#mediante pseudocódigo y el utilizando el ciclo apropiado.

# Inicializar las variables
totalPago = 0
pagoMen = 10
#Se realiza el ciclo for
for i in range(1,21,1):

    totalPago += pagoMen
    print("El pago del mes", i, "es de: ", pagoMen)
    pagoMen=pagoMen*2
    
print("El total de lo que ha pagado después de ", i, "meses es de: ", totalPago)






















