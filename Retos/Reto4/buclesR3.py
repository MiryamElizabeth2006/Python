import re

def es_entero(cadena):
    """Verifica si la cadena representa un número entero."""
    return bool(re.match(r"^-?\d+$", cadena))

def es_decimal(cadena):
    """Verifica si la cadena representa un número decimal."""
    return bool(re.match(r"^-?\d+(\.\d+)?$", cadena))

datos = [] 

try:
    cantidad = int(input("¿Cuántos datos desea ingresar? "))
except ValueError:
    print("Por favor, ingrese un número entero válido.")


for i in range(cantidad):
        entrada = input(f"Ingrese el dato {i + 1}: ")
        
        if es_entero(entrada):
            datos.append(int(entrada))
        elif es_decimal(entrada):
            datos.append(float(entrada))
        else:
            datos.append(entrada)
        

print(f"Su lista es: {datos}")
