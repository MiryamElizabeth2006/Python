
nombre_paciente = []
edad = []

def agregar_nombre(nombre):

    nombre_paciente.append(nombre)

def agregar_edad(año_nacimiento):
    año_actual = 2023
    edad_actual = año_actual - año_nacimiento
    edad.append(edad_actual)

def obtener_mayor_menor():
    mayor = max(edad)
    menor = min(edad)

    paciente_mayor = nombre_paciente[edad.index(mayor)]
    paciente_menor = nombre_paciente[edad.index(menor)]

    return paciente_mayor, mayor, paciente_menor, menor