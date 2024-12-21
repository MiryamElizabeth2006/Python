pais = input("Elige un país (Ecuador - Colombia - Perú): ")
zona = input("Elige la zona (urbana - rural - perimetral): ")
velocidad = int(input("Ingresa la velocidad del conductor (Km/h): "))

# Validar límites según país y zona
if pais == "Ecuador":
    if zona == "urbana":
        if velocidad < 10:
            print("La velocidad está por debajo del límite permitido en la zona urbana de Ecuador.")
        elif velocidad > 50:
            print("La velocidad excede el límite permitido en la zona urbana de Ecuador.")
        else:
            print("La velocidad es adecuada en la zona urbana de Ecuador.")
    elif zona == "rural":
        if velocidad < 51:
            print("La velocidad está por debajo del límite permitido en la zona rural de Ecuador.")
        elif velocidad > 70:
            print("La velocidad excede el límite permitido en la zona rural de Ecuador.")
        else:
            print("La velocidad es adecuada en la zona rural de Ecuador.")
    elif zona == "perimetral":
        if velocidad < 71:
            print("La velocidad está por debajo del límite permitido en la zona perimetral de Ecuador.")
        elif velocidad > 90:
            print("La velocidad excede el límite permitido en la zona perimetral de Ecuador.")
        else:
            print("La velocidad es adecuada en la zona perimetral de Ecuador.")
    else:
        print("Zona no válida para Ecuador.")

elif pais == "Colombia":
    if zona == "urbana":
        if velocidad < 10:
            print("La velocidad está por debajo del límite permitido en la zona urbana de Colombia.")
        elif velocidad > 30:
            print("La velocidad excede el límite permitido en la zona urbana de Colombia.")
        else:
            print("La velocidad es adecuada en la zona urbana de Colombia.")
    elif zona == "rural":
        if velocidad < 31:
            print("La velocidad está por debajo del límite permitido en la zona rural de Colombia.")
        elif velocidad > 80:
            print("La velocidad excede el límite permitido en la zona rural de Colombia.")
        else:
            print("La velocidad es adecuada en la zona rural de Colombia.")
    elif zona == "perimetral":
        if velocidad < 81:
            print("La velocidad está por debajo del límite permitido en la zona perimetral de Colombia.")
        elif velocidad > 100:
            print("La velocidad excede el límite permitido en la zona perimetral de Colombia.")
        else:
            print("La velocidad es adecuada en la zona perimetral de Colombia.")
    else:
        print("Zona no válida para Colombia.")

elif pais == "Perú":
    if zona == "urbana":
        if velocidad < 10:
            print("La velocidad está por debajo del límite permitido en la zona urbana de Perú.")
        elif velocidad > 40:
            print("La velocidad excede el límite permitido en la zona urbana de Perú.")
        else:
            print("La velocidad es adecuada en la zona urbana de Perú.")
    elif zona == "rural":
        if velocidad < 41:
            print("La velocidad está por debajo del límite permitido en la zona rural de Perú.")
        elif velocidad > 60:
            print("La velocidad excede el límite permitido en la zona rural de Perú.")
        else:
            print("La velocidad es adecuada en la zona rural de Perú.")
    elif zona == "perimetral":
        if velocidad < 61:
            print("La velocidad está por debajo del límite permitido en la zona perimetral de Perú.")
        elif velocidad > 120:
            print("La velocidad excede el límite permitido en la zona perimetral de Perú.")
        else:
            print("La velocidad es adecuada en la zona perimetral de Perú.")
    else:
        print("Zona no válida para Perú.")

else:
    print("País no válido.")
