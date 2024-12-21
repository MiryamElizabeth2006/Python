
from clase1 import laptop
from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business


laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)


laptop_juanito = Laptop_Gaming("MSI", "i7", 4, "RTX 8GB")

#laptop_empresa = Laptop_Business(
    #marca="Lenovo",
    #procesador="Intel i5",
    #memoria=16,
    #costo=750,
    #impuesto=15,
    #almacenamiento=512,
    #duracion_bateria=10
#)

def imprimir_informe(Laptop):
 informe = laptop.realizar_informe_uso()
 for clave, valor in informe.items():
    print(f"{clave} : {valor}")
 print({"\n"})

#for numero in range(1,1001):
 #   asus_laptop = Laptop.asus_laptop(numero)
 
#print(laptop_pepito.__dict__)
#print(laptop_pepito.valor_final())
#print(f"el valor de descuento: {laptop_pepito.valor_descuento(10)}")
#print(Laptop.comparar_costo(laptop_pepito, laptop_maria))
#print(asus_laptop.__dict__)
#print(laptop_juanito.realizar_diagnostico_sistema())

#diagnostico = laptop_empresa.realizar_diagnostico_sistema()
#print(diagnostico)

print("PEPITO: ")
imprimir_informe(laptop_pepito)

print("JUANITO: ")
imprimir_informe(laptop_juanito)
