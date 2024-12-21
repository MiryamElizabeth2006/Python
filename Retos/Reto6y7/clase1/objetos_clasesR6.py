from datetime import datetime
#Reto 6
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

#Reto 7
    @classmethod
    def crear_auto_toyota(cls, modelo):
     año_actual = datetime.now().year
     marca="Toyota"
     modelo=modelo
     return cls(marca, modelo, año_actual)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
      if auto1.kilometraje == auto2.kilometraje:
       return "Los autos tienen el mismo kilometraje"
      else:
       return "Los autos tienen diferente kilometraje"

    @staticmethod
    def estado_auto(kilometraje):
      if kilometraje < 20000:
        return "Estoy como nuevo"
      elif 20000 <= kilometraje <= 100000:
        return "Ya estoy usado"
      else:
        return "¡Ya déjame descansar por favor!"

    @classmethod
    def auto_de_segunda(cls, modelo, kilometraje):
        año_actual = datetime.now().year - 3  # Suponemos que tiene 3 años de antigüedad
        return cls(marca="Toyota", modelo=modelo, año=año_actual, kilometraje=kilometraje)