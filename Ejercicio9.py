# Diseñar un diagrama que permita emitir la factura correspondiente a una compra de un
# artículo del cual se adquiere una o varias unidades y se conoce su precio antes de IVA (iva igual
# al 16%), y si el precio bruto (precio de venta más IVA) es mayor de $500. 000.oo se debe realizar
# un descuento del 15%.

# Se pide cunatas compras realizo
num_com = int(input("Ingrese el numero de compras: "))
# Se agrega el for para poder realizar todo el proceso
for i in range(num_com):
    print(f"Compra {i+1}:")
    precioU= float(input("Ïngrese el valor de la compra antes del IVA: "))
    cant = int(input("Ingrese la cantidad de unidades: "))
#Se realiza la operacion para agg el IVa
    subtotal = precioU * cant
    iva = subtotal * 0.16
    precio_bruto = subtotal + iva   
# Se realiza la condicional if
    if precio_bruto > 500000:
     descuento = precio_bruto * 0.15
else:
    descuento = 0

totalPagar = precio_bruto - descuento
# Se muestra todos los resultados
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Precio bruto: ${precio_bruto:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${totalPagar:.2f}\n")