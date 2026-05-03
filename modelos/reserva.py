from excepciones.excepciones import *
import logging

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):
        try:
            if self.duracion <= 0:
                raise DuracionInvalidaError("Duración inválida")

            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            logging.info(f"Reserva confirmada para {self.cliente.nombre}")
            return costo

        except Exception as e:
            logging.error(f"Error al confirmar reserva: {e}")
            raise ReservaError("No se pudo confirmar la reserva") from e

        finally:
            logging.info("Proceso de confirmación ejecutado")

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        logging.info(f"Reserva cancelada de {self.cliente.nombre}")