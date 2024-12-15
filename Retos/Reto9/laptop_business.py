from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10, almacenamiento=256, duracion_bateria=8):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def __str__realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_diagnostico["ALMACENAMIENTO"] = f"{self.almacenamiento} GB"
        resultado_diagnostico["DURACIÓN DE BATERÍA"] = f"{self.duracion_bateria} horas"
        resultado_diagnostico["CONEXIÓN DE RED"] = self.verificar_conectividad_red()
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia aceptable": random.choice([True, False]),
        }
        return conectividad



