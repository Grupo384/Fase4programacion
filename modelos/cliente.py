"""
Módulo Cliente — Software FJ
Persona 1: Clase Cliente con validaciones y encapsulación
"""

import re
from modelos.entidad_base import EntidadBase
from excepciones.excepciones import ClienteInvalidoError


class Cliente(EntidadBase):
    """Clase que representa un cliente del sistema Software FJ."""

    def __init__(self, nombre, email, telefono):
        super().__init__()
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío.")
        if len(valor.strip()) < 2:
            raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r"[^@]+@[^@]+\.[^@]+"
        if not valor or not re.match(patron, valor):
            raise ClienteInvalidoError(f"Email inválido: '{valor}'")
        self._email = valor.lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        limpio = str(valor).replace(" ", "").replace("-", "")
        if not limpio.lstrip("+").isdigit() or len(limpio) < 7:
            raise ClienteInvalidoError(f"Teléfono inválido: '{valor}'")
        self._telefono = limpio

    def describir(self):
        return f"Cliente: {self._nombre} | Email: {self._email} | Tel: {self._telefono}"

    def __str__(self):
        return self.describir()