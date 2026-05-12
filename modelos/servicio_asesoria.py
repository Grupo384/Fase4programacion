from modelos.servicio import Servicio


class ServicioAsesoria(Servicio):

    def __init__(self, nombre, precio_base, especialista):
        super().__init__(nombre, precio_base)
        self.especialista = especialista

    def calcular_costo(self, duracion, horas_extra=0):
        return (self.precio_base * duracion) + horas_extra

    def describir_servicio(self):
        return f"Asesoría especializada con {self.especialista}"

    def validar_parametros(self):
        if not self.especialista.strip():
            raise ValueError("Especialista inválido")
