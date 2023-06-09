def login():
    while True:
        print("==== Repair Center - Inicio de Sesión ====")
        usuario = input("Usuario: ")
        clave = input("Contraseña: ")

        # Verificar las credenciales (usuario y clave)
        if usuario == "admin" and clave == "admin123":
            print("Inicio de sesión exitoso.\n")
            break
        else:
            print("Credenciales incorrectas. Intente nuevamente.\n")