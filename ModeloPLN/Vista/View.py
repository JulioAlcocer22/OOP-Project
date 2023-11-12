def opcion_1():
    print("Has seleccionado la Opción 1.")
    # Coloca aquí el código correspondiente a la Opción 1

def opcion_2():
    print("Has seleccionado la Opción 2.")
    # Coloca aquí el código correspondiente a la Opción 2

while True:
    print("\nMenú:")
    print("1. Realizar la Opción 1")
    print("2. Realizar la Opción 2")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
