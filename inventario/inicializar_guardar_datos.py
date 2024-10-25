import json
import os

# Ruta del archivo JSON
def ruta_json():
    return "datos/inventario.json"

# Cargar inventario desde el archivo JSON
def cargar_inventario():
    if os.path.exists(ruta_json()):
        with open(ruta_json(), 'r') as file:
            return json.load(file)
    else:
        return {}

# Guardar inventario en el archivo JSON
def guardar_inventario(inventario):
    with open(ruta_json(), 'w') as file:
        json.dump(inventario, file, indent=4)