# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de
# cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva
# ahorrado cada mes.
# Se hace el contador
totalAhor= 0
# se aplica la condicional for
for mes in range(1, 13):
    deposito =float (input(f"Igresa la cantidad despositada en el mes{mes}: "))
    totalAhor += deposito
    print(f"Total ahorrado hasta el mes{mes}: {totalAhor} Pesos")
print(f"EL ahorro total en el año es: {totalAhor} Pesos")
