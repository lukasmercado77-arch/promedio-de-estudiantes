saldo = 10000000

while True:
    print("\n=== CAJERO ===")
    print("1. Ver saldo")
    print("2. Consignar dinero")
    print("3. Sacar dinero")
    print("4. Terminar")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        print("Su dinero disponible es: $", saldo)

    elif opcion == "2":
        valor = float(input("¿Cuánto desea consignar?: "))

        if valor > 0:
            saldo += valor
            print("Consignación exitosa")
        else:
            print("Ingrese un valor válido")

    elif opcion == "3":
        valor = float(input("¿Cuánto desea retirar?: "))

        if valor <= 0:
            print("Ingrese un valor válido")
        elif valor > saldo:
            print("No tiene suficiente dinero")
        else:
            saldo -= valor
            print("Retiro exitoso")

    elif opcion == "4":
        print("Gracias por utilizar el cajero")
        break

    else:
        print("Opción incorrecta")

    print("Saldo actual: $", saldo)