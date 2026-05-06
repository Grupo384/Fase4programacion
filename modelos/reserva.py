"""
Módulo Reserva — Software FJ
Persona 3: Clase Reserva — integra Cliente y Servicio
Métodos: confirmar, cancelar, procesar
"""

import logging
from modelos.entidad_base import EntidadBase
from excepciones.excepciones import ReservaError, DuracionInvalidaError, ServicioNoDisponibleError

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Reserva(EntidadBase):
    """Clase que gestiona la reserva de un servicio para un cliente."""

    def __init__(self, cliente, servicio, duracion):
        super().__init__()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "pendiente"
        self._costo_final = None

    def confirmar_reserva(self):
        try:
            if self._estado != "pendiente":
                raise ReservaError(
                    f"No se puede confirmar una reserva en estado '{self._estado}'."
                )
            if not self._servicio.disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio '{self._servicio._nombre}' no está disponible."
                )
            if self._duracion <= 0:
                raise DuracionInvalidaError("La duración debe ser mayor a 0 horas.")
            self._estado = "confirmada"
            logging.info(f"Reserva confirmada para {self._cliente.nombre}")
            return True
        except (ReservaError, ServicioNoDisponibleError, DuracionInvalidaError):
            logging.error(f"Error al confirmar reserva de {self._cliente.nombre}")
            raise
        finally:
            logging.info("Proceso de confirmacion ejecutado.")

    def cancelar_reserva(self, motivo="Sin motivo"):
        try:
            if self._estado == "cancelada":
                raise ReservaError("La reserva ya fue cancelada.")
            if self._estado == "procesada":
                raise ReservaError("No se puede cancelar una reserva ya procesada.")
            self._estado = "cancelada"
            logging.info(f"Reserva cancelada: {self._cliente.nombre} - {motivo}")
            return f"Reserva cancelada. Motivo: {motivo}"
        except ReservaError:
            logging.error(f"Error al cancelar reserva de {self._cliente.nombre}")
            raise

    def procesar_reserva(self, con_iva=False, descuento=0):
        try:
            if self._estado != "confirmada":
                raise ReservaError("Solo se pueden procesar reservas confirmadas.")
            self._costo_final = self._servicio.calcular_costo(
                self._duracion, con_iva, descuento
            )
            self._estado = "procesada"
            logging.info(
                f"Reserva procesada: {self._cliente.nombre} | ${self._costo_final:,.0f}"
            )
            return self._costo_final
        except Exception:
            logging.error(f"Error al procesar reserva de {self._cliente.nombre}")
            raise
        finally:
            logging.info("Proceso de procesamiento ejecutado.")

    def describir(self):
        costo = f"${self._costo_final:,.0f}" if self._costo_final else "Pendiente"
        return (
            f"Reserva [{self._estado.upper()}]\n"
            f"  Cliente : {self._cliente.nombre}\n"
            f"  Servicio: {self._servicio.describir_servicio()}\n"
            f"  Duracion: {self._duracion}h | Costo: {costo}"
        )

    def __str__(self):
        return self.describir()