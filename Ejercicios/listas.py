# Listas
planetas = [
    "Mercurio",
    "Venus",
    "Tierra",
    "Marte",
    "Júpiter",
    "Saturno",
    "Urano",
    "Neptuno"
]
#Listas print(planetas[2])
#Sublistas print(planetas[1: 6])
print(len(planetas))

#Gravedad de los planetas
gravedades = [
    3.7,   # Mercurio
    8.87,  # Venus
    9.8,   # Tierra
    3.71,  # Marte
    24.79, # Júpiter
    10.44, # Saturno
    8.69,  # Urano
    11.15  # Neptuno
]

peso_bus = 125213 #Newtons, en la la tierra

print(f"En la tierra , un autobus de dos pisos pesa {peso_bus} N")
print(f"En mercurio, un autobus de dos pisos pesa {peso_bus * gravedades[0]} N")

print(f"Lo más liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedades)}")
print(f"Lo mas pesado  que seria un autobus en el sistema solar es {peso_bus * max(gravedades)}")