# Ejercicio 1: Contar cuántas vocales tiene una palabra o frase
frase = input("Ingresa una palabra o frase: ")
vocales = "aeiouAEIOU"
contar_a = 0
contar_e = 0
contar_i = 0
contar_o = 0
contar_u = 0

for letra in frase:
    if letra == "a" or letra == "A":
        contar_a += 1
    if letra == "e" or letra == "E":
        contar_e += 1
    if letra == "i" or letra == "I":
        contar_i += 1
    if letra == "o" or letra == "O":
        contar_o += 1
    if letra == "u" or letra == "U":
        contar_u += 1

print("Vocal A:", contar_a)
print("Vocal E:", contar_e)
print("Vocal I:", contar_i)
print("Vocal O:", contar_o)
print("Vocal U:", contar_u)
