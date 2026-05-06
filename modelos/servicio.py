"""
Módulo Servicio — Software FJ
Persona 2: Clase abstracta Servicio y 3 subclases especializadas
Aplica: Herencia, Polimorfismo, Métodos sobrescritos
"""

from abc import abstractmethod
from modelos.entidad_base import EntidadBase
from excepciones.excepciones import ServicioNoDisponibleError


class Servicio(EntidadBase):
    """Clase abstracta base para todos los servicios de Software FJ."""

    TARIFA_IVA = 0.19  # 19% IVA Colombia

    def __init__(self, nombre, precio_base, disponible=True):
        super().__init__()
        if precio_base <= 0:
            raise ServicioNoDisponibleError("El precio base debe ser mayor a 0.")
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion, con_iva=False, descuento=0):
        """Cada servicio calcula su costo de forma diferente — Polimorfismo."""
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    def _aplicar_modificadores(self, costo_base, con_iva, descuento):
        """Aplica IVA y descuento al costo base."""
        if not (0 <= descuento <= 100):
            raise ServicioNoDisponibleError("El descuento debe estar entre 0 y 100.")
        costo = costo_base * (1 - descuento / 100)
        if con_iva:
            costo *= (1 + self.TARIFA_IVA)
        return round(costo, 2)

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    def describir(self):
        return self.describir_servicio()

    def __str__(self):
        return self.describir_servicio()


# ── SUBCLASES ────────────────────────────────────────────────────────────────

class ReservaSala(Servicio):
    """Servicio de reserva de salas de reunión."""

    def __init__(self, capacidad=10):
        super().__init__("Reserva de Sala", precio_base=50000)
        if capacidad < 1:
            raise ServicioNoDisponibleError("La capacidad debe ser al menos 1 persona.")
        self._capacidad = capacidad

    def calcular_costo(self, duracion, con_iva=False, descuento=0):
        base = self._precio_base * duracion
        return self._aplicar_modificadores(base, con_iva, descuento)

    def describir_servicio(self):
        return f"Sala de reunión | Capacidad: {self._capacidad} personas | $50.000/hora"

    def validar_parametros(self):
        return self._capacidad >= 1 and self._precio_base > 0


class AlquilerEquipos(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    TIPOS_VALIDOS = {"laptop", "proyector", "camara", "tablet"}

    def __init__(self, tipo_equipo="laptop"):
        super().__init__("Alquiler de Equipos", precio_base=30000)
        if tipo_equipo.lower() not in self.TIPOS_VALIDOS:
            raise ServicioNoDisponibleError(
                f"Tipo de equipo inválido. Opciones: {self.TIPOS_VALIDOS}"
            )
        self._tipo_equipo = tipo_equipo.lower()

    def calcular_costo(self, duracion, con_iva=False, descuento=0):
        multiplicador = 1.5 if self._tipo_equipo == "proyector" else 1.0
        base = self._precio_base * duracion * multiplicador
        return self._aplicar_modificadores(base, con_iva, descuento)

    def describir_servicio(self):
        return f"Alquiler: {self._tipo_equipo} | $30.000/hora base"

    def validar_parametros(self):
        return self._tipo_equipo in self.TIPOS_VALIDOS


class AsesoriaTecnica(Servicio):
    """Servicio de asesoría técnica especializada."""

    def __init__(self, especialidad="General"):
        super().__init__("Asesoría Técnica", precio_base=120000)
        self._especialidad = especialidad

    def calcular_costo(self, duracion, con_iva=False, descuento=0):
        # Más de 3 horas tiene tarifa reducida
        if duracion > 3:
            base = self._precio_base * 3 + (self._precio_base * 0.8) * (duracion - 3)
        else:
            base = self._precio_base * duracion
        return self._aplicar_modificadores(base, con_iva, descuento)

    def describir_servicio(self):
        return f"Asesoría {self._especialidad} | $120.000/hora"

    def validar_parametros(self):
        return len(self._especialidad) > 0