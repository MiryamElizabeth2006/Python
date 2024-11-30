
class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, kilometraje: {self.kilometraje}")

    def actualizar_kilometraje(self, nuevo_kilometraje):
      if nuevo_kilometraje >= self.kilometraje:
       self.kilometraje = nuevo_kilometraje
       return (f"El kilometraje se ha actualizado a {self.kilometraje} km.")
      else:
       return ("Error: No se puede reducir el kilometraje.")

    def realizar_viaje(self, kilometros):
     if kilometros > 0:
      self.kilometraje += kilometros
      return (f"Has realizado un viaje de {kilometros} km. Kilometraje actual: {self.kilometraje} km.")
     else: 
      return ("Error: La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
      if self.kilometraje < 20000:
       return ("Estoy como nuevo")
      elif 20000 <= self.kilometraje <= 100000:
       return ("Ya estoy usado")
      else: 
       return ("Ya dejame descansar por favor")

      
mi_auto = Auto("Toyota", "Corolla", 2022)

print(mi_auto.mostrar_informacion())
print(mi_auto.actualizar_kilometraje(50))
print(mi_auto.realizar_viaje(200000))
print(mi_auto.estado_auto())
