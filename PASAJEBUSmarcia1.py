adisponibles = [1, 2, 3, 4, 5]
while True:
    print("** SISTEMA DE PASAJES PASAJEBUS **")
    print("1. Ver asientos disponibles")
    print("2. Comprar pasaje")
    print("3. Salir")
    opcion = input("seleccione una opcion (1-3): ")
    if opcion == "1":
        print("asientos disponibles:", adisponibles)
    elif opcion == "2":
        try:
            asiento = int(input("Ingrese el numero de asiento que desea comprar: "))
            if asiento in adisponibles:
                adisponibles.remove(asiento)
                print(f"asiento {asiento} comprado exitosamente")
            else:
                print("ese asiento no esta disponible")
        except ValueError:
            print("ingrese un numero valido")
    elif opcion == "3":
        print("saliendo del sistema, gracias por usar pasajebus")
        break
    else:
        print("opcion invalida, intente nuevamente")