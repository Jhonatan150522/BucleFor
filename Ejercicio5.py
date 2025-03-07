# Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere saber cuántas
# de ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a
# $1000, y cuántas fueron menores o iguales a $500. Además, se requiere saber el monto de lo
# vendido en cada categoría y de forma global. Realice un algoritmo que permita determinar lo
# anterior. 

# Se le pide al usuario que ingresa la cantida de ventas
Ventas= int(input("Ingrese la cantodad de ventas: "))
# se relaiza los contadores y las listas para ir agregando
# Se realiza lista y contador para ventas entre 500 y 1000
entremilyqui= []
cont_500_100= 0
# Se realiza lista y contenedor para ventas mayores de 1000 
mayormil= []
cont_mayor_100= 0
# Se realiza lista y contenedor para ventas menores de 500
menorqui = []
cont_menores_500 = 0

# Se realiza el buccle for para pasar cada venta y tambien para procesar cada valor de la venta

for i in range (Ventas):
# Se realiza una variable para poder ssaber el valor de la venta
    valor =int(input("Digite el valor de la venta: "))
    if valor > 500 and valor < 1000:
        cont_500_100+=1
        entremilyqui.append(valor)
    elif valor > 1000:
        cont_mayor_100+=1
        mayormil.append(valor)
    elif valor < 500:
        cont_menores_500	+=1
        menorqui.append(valor)
# Se realiza las variables totales de los valores de la venta
totalEntreMilyquientos=sum(entremilyqui)
totalVentaMayor= sum(mayormil)
totalVentamenor500= sum(menorqui)
TotalTodo= totalEntreMilyquientos + totalVentaMayor + totalVentamenor500
# Se muestran todos los resultados
print("\nResumen de ventas del día:")
print(f"La cantidad de ventas entre $500 y $1000 es: {cont_500_100}, con un total de: ${totalEntreMilyquientos}")
print(f"La cantidad de ventas mayores de $1000 es: {cont_mayor_100}, con un total de: ${totalVentaMayor}")
print(f"La cantidad de ventas menores o iguales a $500 es: {cont_menores_500}, con un total de: ${totalVentamenor500}")
print(f"El total de todas las ventas es: ${TotalTodo}")



