"""
Módulo de excepciones personalizadas — Software FJ
Persona 4: Manejo avanzado de errores
"""

# ── EXCEPCIONES PERSONALIZADAS ───────────────────────────────────────────────

class SistemaError(Exception):
    """Excepción base del sistema."""
    def __init__(self, mensaje, codigo=None):
        super().__init__(mensaje)
        self.codigo = codigo
        self.mensaje = mensaje

    def __str__(self):
        prefijo = f"[{self.codigo}] " if self.codigo else ""
        return f"{prefijo}{self.mensaje}"


class ClienteInvalidoError(SistemaError):
    """Datos de cliente inválidos."""
    def __init__(self, mensaje):
        super().__init__(mensaje, codigo="ERR-CLI")


class ServicioNoDisponibleError(SistemaError):
    """Servicio no disponible o con parámetros incorrectos."""
    def __init__(self, mensaje):
        super().__init__(mensaje, codigo="ERR-SRV")


class ReservaError(SistemaError):
    """Operación de reserva inválida."""
    def __init__(self, mensaje):
        super().__init__(mensaje, codigo="ERR-RES")


class DuracionInvalidaError(SistemaError):
    """Duración de reserva inválida."""
    def __init__(self, mensaje):
        super().__init__(mensaje, codigo="ERR-DUR")


# ── FUNCIÓN DE CONTROL CON try/except/else/finally ───────────────────────────

def ejecutar_con_control(operacion, descripcion, logger=None):
    """
    Ejecuta cualquier operación con manejo completo de excepciones.
    Implementa: try / except / else / finally
    """
    resultado = None
    try:
        resultado = operacion()

    except ClienteInvalidoError as e:
        msg = f"Error de cliente — {descripcion}: {e}"
        print(f"  ✗ {msg}")
        if logger:
            logger.registrar_error(msg)

    except ServicioNoDisponibleError as e:
        msg = f"Error de servicio — {descripcion}: {e}"
        print(f"  ✗ {msg}")
        if logger:
            logger.registrar_error(msg)

    except ReservaError as e:
        msg = f"Error de reserva — {descripcion}: {e}"
        print(f"  ✗ {msg}")
        if logger:
            logger.registrar_error(msg)

    except DuracionInvalidaError as e:
        msg = f"Error de duración — {descripcion}: {e}"
        print(f"  ✗ {msg}")
        if logger:
            logger.registrar_error(msg)

    except Exception as e:
        msg = f"Error inesperado — {descripcion}: {type(e).__name__}: {e}"
        print(f"  ✗ {msg}")
        if logger:
            logger.registrar_error(msg)

    else:
        # Se ejecuta SOLO si no hubo ninguna excepción
        print(f"  ✓ {descripcion} — OK")

    finally:
        # Se ejecuta SIEMPRE, haya o no error
        pass

    return resultado