from modelos.cliente import Cliente
from registros.logs import registrar_log

def prueba_clientes():
    print("Creando clientes...")

    try:
        c1 = Cliente("Juan Perez", "juan@email.com", "123456")
        print(c1.mostrar_info())

        # Cliente inválido para probar excepciones
        c2 = Cliente("", "correo_invalido", "abc")

    except Exception as e:
        print("Error capturado:", e)
        registrar_log(str(e), "ERROR")
    else:
        registrar_log("Clientes creados correctamente", "INFO")

    finally:
        registrar_log("Finalizó prueba_clientes()", "INFO")
if __name__ == "__main__":
    prueba_clientes()
