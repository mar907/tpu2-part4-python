def ingresar_pedido():
    apellido_nombre = input("Ingrese el apellido y nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente (calle y altura): ")
    inconveniente = input("Ingrese el inconveniente reportado: ")
    tecnico_asignado = input("Ingrese el nombre del técnico asignado: ")
    fecha_visita = input("Ingrese la fecha y hora de la visita (YYYY-MM-DD HH:MM): ")

    # Guardar los datos en un archivo
    with open("pedidos.txt", "a") as archivo:
        archivo.write("Apellido y Nombre del Cliente: {}\n".format(apellido_nombre))
        archivo.write("Dirección: {}\n".format(direccion))
        archivo.write("Inconveniente: {}\n".format(inconveniente))
        archivo.write("Técnico Asignado: {}\n".format(tecnico_asignado))
        archivo.write("Fecha de Visita: {}\n".format(fecha_visita))
        archivo.write("=================================\n")

    print("Pedido ingresado con éxito.")


def mostrar_pedidos():
    try:
        # Leer el archivo con los pedidos
        with open("pedidos.txt", "r") as archivo:
            pedidos = archivo.read()
            print(pedidos)
    except FileNotFoundError:
        print("No hay pedidos ingresados.")