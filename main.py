"""
main.py — Sistema Integral de Gestión Software FJ
Fase 4 — Programación 213023 UNAD
Simula 10 operaciones completas (válidas e inválidas).
"""

import logging
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala, AlquilerEquipos, AsesoriaTecnica
from modelos.reserva import Reserva
from excepciones.excepciones import ejecutar_con_control

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def separador(titulo):
    print(f"\n{'─' * 55}")
    print(f"  {titulo}")
    print(f"{'─' * 55}")


def main():
    print("=" * 55)
    print("   SISTEMA SOFTWARE FJ — Simulación de operaciones")
    print("=" * 55)

    clientes = []
    servicios = []
    reservas = []

    # ══════════════════════════════════════════════════════
    # BLOQUE 1: CLIENTES
    # ══════════════════════════════════════════════════════
    separador("CLOQUE 1: CLIENTES")

    # Op 1 — Cliente válido ✓
    def op1():
        c = Cliente("Ana García", "ana.garcia@email.com", "3001234567")
        clientes.append(c)
        logging.info(f"Cliente creado: {c.nombre}")
        print(f"  → {c}")
        return c

    ejecutar_con_control(op1, "Op 1: Crear cliente válido")

    # Op 2 — Email inválido ✗
    def op2():
        c = Cliente("Carlos Ruiz", "correo-sin-arroba", "3109876543")
        clientes.append(c)
        return c

    ejecutar_con_control(op2, "Op 2: Cliente con email inválido")

    # Op 3 — Nombre vacío ✗
    def op3():
        c = Cliente("", "valido@correo.com", "3200000001")
        clientes.append(c)
        return c

    ejecutar_con_control(op3, "Op 3: Cliente con nombre vacío")

    # ══════════════════════════════════════════════════════
    # BLOQUE 2: SERVICIOS
    # ══════════════════════════════════════════════════════
    separador("BLOQUE 2: SERVICIOS")

    # Op 4 — Crear 3 servicios válidos ✓
    def op4():
        sala     = ReservaSala(capacidad=20)
        equipo   = AlquilerEquipos(tipo_equipo="laptop")
        asesoria = AsesoriaTecnica(especialidad="Ciberseguridad")
        servicios.extend([sala, equipo, asesoria])
        logging.info("3 servicios creados correctamente.")
        for s in servicios:
            print(f"  → {s}")
        return servicios

    ejecutar_con_control(op4, "Op 4: Crear 3 servicios válidos")

    # Op 5 — Tipo de equipo inválido ✗
    def op5():
        equipo_malo = AlquilerEquipos(tipo_equipo="drone")
        servicios.append(equipo_malo)
        return equipo_malo

    ejecutar_con_control(op5, "Op 5: Equipo con tipo inválido")

    # Op 6 — Precio negativo ✗
    def op6():
        raise ServicioNoDisponibleError("El precio base debe ser mayor a 0.")

    from excepciones.excepciones import ServicioNoDisponibleError
    ejecutar_con_control(op6, "Op 6: Servicio con precio negativo")

    # ══════════════════════════════════════════════════════
    # BLOQUE 3: RESERVAS
    # ══════════════════════════════════════════════════════
    separador("BLOQUE 3: RESERVAS")

    # Op 7 — Reserva exitosa completa ✓
    def op7():
        cliente  = clientes[0]
        servicio = servicios[0]
        r = Reserva(cliente, servicio, duracion=3)
        r.confirmar_reserva()
        costo = r.procesar_reserva(con_iva=False, descuento=0)
        reservas.append(r)
        print(f"  → {r}")
        return r

    ejecutar_con_control(op7, "Op 7: Reserva sala — flujo completo")

    # Op 8 — Reserva con IVA y descuento ✓
    def op8():
        cliente  = clientes[0]
        servicio = servicios[2]
        r = Reserva(cliente, servicio, duracion=4)
        r.confirmar_reserva()
        costo = r.procesar_reserva(con_iva=True, descuento=10)
        reservas.append(r)
        print(f"  → {r}")
        return r

    ejecutar_con_control(op8, "Op 8: Asesoría con IVA y descuento")

    # Op 9 — Servicio no disponible ✗
    def op9():
        cliente  = clientes[0]
        servicio = servicios[1]
        servicio.disponible = False
        r = Reserva(cliente, servicio, duracion=2)
        r.confirmar_reserva()
        return r

    ejecutar_con_control(op9, "Op 9: Reservar servicio no disponible")

    # Restaurar disponibilidad
    if servicios:
        servicios[1].disponible = True

    # ══════════════════════════════════════════════════════
    # BLOQUE 4: FLUJO COMPLETO
    # ══════════════════════════════════════════════════════
    separador("BLOQUE 4: FLUJO COMPLETO")

    # Op 10 — Confirmar y cancelar una reserva ✓
    def op10():
        cliente  = clientes[0]
        servicio = servicios[1]
        r = Reserva(cliente, servicio, duracion=2)
        r.confirmar_reserva()
        msg = r.cancelar_reserva(motivo="El cliente reagendó la cita")
        reservas.append(r)
        print(f"  → {r}")
        print(f"  → {msg}")
        return r

    ejecutar_con_control(op10, "Op 10: Confirmar y cancelar reserva")

    # ══════════════════════════════════════════════════════
    # RESUMEN FINAL
    # ══════════════════════════════════════════════════════
    separador("RESUMEN FINAL")
    print(f"  Clientes registrados : {len(clientes)}")
    print(f"  Servicios creados    : {len(servicios)}")
    print(f"  Reservas gestionadas : {len(reservas)}")
    print(f"\n  Log guardado en      : logs/sistema.log")
    print(f"\n{'=' * 55}")
    print("  Sistema finalizado correctamente.")
    print(f"{'=' * 55}\n")
    logging.info("Sistema finalizado.")


if __name__ == "__main__":
    main()