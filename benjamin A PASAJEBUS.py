nombres_disponibles = ["Ana", "Luis", "Carlos", "Sofía", "Marta"]
opcion = 0

while opcion != 3:
    print("***** Sistema de nombres disponibles *****")
    print("1.- Ver nombres disponibles")
    print("2.- Seleccionar un nombre")
    print("3.- Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Nombres disponibles:", nombres_disponibles)

    elif opcion == 2:
        nombre = input("Ingrese el nombre que desea seleccionar: ").capitalize()
        if nombre in nombres_disponibles:
            nombres_disponibles.remove(nombre)
            print("El nombre", nombre, "ha sido seleccionado correctamente.")
        else:
            print("Ese nombre no está disponible o ya fue seleccionado.")

    elif opcion == 3:
        print("Saliendo del sistema...")

    else:
        print("Opción no válida. Intente nuevamente.")

