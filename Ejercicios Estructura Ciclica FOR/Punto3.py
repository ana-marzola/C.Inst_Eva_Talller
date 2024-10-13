# Ejercicio 3: Imprimir palabras que comienzan con una letra específica
palabras = input("Ingresa una lista de palabras separadas por comas: ").split(",")
letra = input("Ingresa la letra con la que deben comenzar las palabras: ")

print(f"Palabras que comienzan con '{letra}':")
for palabra in palabras:
    if palabra.startswith(letra):
        print(palabra)