from modelos.servicio import Servicio


class ServicioSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, duracion, descuento=0):
        costo = self.precio_base * duracion
        return costo - descuento

    def describir_servicio(self):
        return f"Sala con capacidad para {self.capacidad} personas"

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise ValueError("Capacidad inválida")
