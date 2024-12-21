from informacionR5 import agregar_nombre, agregar_edad, obtener_mayor_menor, nombre_paciente, edad

for _ in range(12):
    datos = input("Ingrese el nombre y año de nacimiento (ejemplo: Antonio Moreno 2000): ")
    partes = datos.split()
    nombre = ' '.join(partes[:-1])  
    año_nacimiento = int(partes[-1])  
    agregar_nombre(nombre)
    agregar_edad(año_nacimiento)

print("Lista de nombres de pacientes:")
print(nombre_paciente)

print("Lista de edades de pacientes:")
print(edad)

paciente_mayor, edad_mayor, paciente_menor, edad_menor = obtener_mayor_menor()

print(f"{paciente_mayor} con la edad de {edad_mayor} años es mayor a los demás pacientes.")
print(f"{paciente_menor} con la edad de {edad_menor} años es menor a los demás pacientes.")

