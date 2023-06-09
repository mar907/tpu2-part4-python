from pedidos_app.login import login
from pedidos_app.funciones_pedidos import ingresar_pedido, mostrar_pedidos

def main():
    while True:
        print("==== Repair Center - Administración de Pedidos ====")
        print("1. Ingresar Pedido")
        print("2. Mostrar Pedidos")
        print("3. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            ingresar_pedido()
        elif opcion == "2":
            mostrar_pedidos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

        print()


if __name__ == "__main__":
    login()
    main()