asientos_disponibles = [1, 2, 3, 4, 5]
opcion = 0
while opcion != 3: 
    print("***** sistema de pasajes pasajebus*****")
    print("1.- ver asientos disponibles")
    print("2.- comprar pasaje")
    print("3.- salir")
    opcion= int(input("seleccione una opcion:"))
    if opcion== 1:
        print("asientos disponibles:", asientos_disponibles)
    elif opcion == 2:
        asientos= int(input("ingrese numero de asiento a comprar:"))
        if asientos in asientos_disponibles:
            asientos_disponibles.remove(asientos)
            print("asiento", asientos, "comprado con exito.")
        else:
            print("ese asiento no esta disponibleo ya fue comprado.")
    elif opcion == 3:
        print("saliendo del sistema...gracias por usar pasajebus.")
    else:
        print("opcion no correcta. intente nuevamnete.")
