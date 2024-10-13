# Ejercicio 4: Sumar los números pares en una lista
numeros = input("Ingresa una lista de números separados por comas: ").split(",")
suma_pares = 0

for num in numeros:
    if int(num) % 2 == 0:
        suma_pares += int(num)

print("La suma de los números pares es:", suma_pares)