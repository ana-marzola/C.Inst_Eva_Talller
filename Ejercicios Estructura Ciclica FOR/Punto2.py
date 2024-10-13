# Ejercicio 2: Ordenar lista de nombres alfabéticamente
nombres = input("Ingresa una lista de nombres separados por comas: ").split(",")
nombres.sort()

print("Nombres en orden alfabético:")
for nombre in nombres:
    print(nombre)
