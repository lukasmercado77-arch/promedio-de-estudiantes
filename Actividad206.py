
lista_de_estudiantes = []


while True:

    print("\n===== MENU PRINCIPAL =====")
    print("1. Registrar estudiante")
    print("2. Finalizar registro")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        nombre = input("Nombre del estudiante: ")

        try:
            Nota_1 = float(input("Nota 1 del estudiante: "))
            Nota_2 = float(input("Nota 2 del estudiante: "))
            Nota_3 = float(input("Nota 3 del estudiante: "))

            if not all(0 <= nota <= 5 for nota in [Nota_1, Nota_2, Nota_3]):
                print("Las notas deben estar entre 0 y 5.")
                continue

        except ValueError:
            print("Nota invalida, intente de nuevo.")
            continue

        promedio_estudiante = (Nota_1 + Nota_2 + Nota_3) / 3

        estudiante = {
            "Nombre": nombre,
            "Nota 1": Nota_1,
            "Nota 2": Nota_2,
            "Nota 3": Nota_3,
            "Promedio": promedio_estudiante
        }
        lista_de_estudiantes.append(estudiante)
        print("Estudiante registrado correctamente.")

    elif opcion == "2":

        print("\n===== RESULTADO FINAL =====")

        ganaron = 0
        perdieron = 0
        for estudiante in lista_de_estudiantes:
            print("\nNombre:", estudiante["Nombre"])

            print("Nota:", estudiante["Nota 1"], "-",
                  estudiante["Nota 2"], "-",
                  estudiante["Nota 3"])

            print("Promedio:", round(estudiante["Promedio"], 2))

            if estudiante["Promedio"] >= 3:
                print("Estudiante: GANO")
                ganaron += 1

            else:
                print("Estudiante: PERDIO")
                perdieron += 1

        if len(lista_de_estudiantes) > 0:

            promedios = [e["Promedio"] for e in lista_de_estudiantes]

            total = len(promedios)

            promedio_grupo = sum(promedios) / total

            porcentaje_aprobados = (ganaron / total) * 100

            todas_las_notas = []

            for e in lista_de_estudiantes:

                for i in (1, 2, 3):

                    todas_las_notas.append(
                        (e["Nota " + str(i)], e["Nombre"], i)
                    )

            nota_maxima = max(todas_las_notas, key=lambda t: t[0])

            nota_minima = min(todas_las_notas, key=lambda t: t[0])

            print("\n===== ESTADISTICAS =====")

            print("Total de estudiantes:", total)

            print("Promedio del grupo:", round(promedio_grupo, 2))

            print("Nota maxima:", nota_maxima[0],
                  "- sacada por", nota_maxima[1],
                  "(Nota", nota_maxima[2], ")")

            print("Nota minima:", nota_minima[0],
                  "- sacada por", nota_minima[1],
                  "(Nota", nota_minima[2], ")")

            print("Estudiantes que ganaron:", ganaron)

            print("Estudiantes que perdieron:", perdieron)

            print("Porcentaje de aprobacion:",
                  round(porcentaje_aprobados, 1), "%")

        else:
            print("\nNo se registraron estudiantes.")

        print("\nRegistro finalizado.")
        break

    else:
        print("\nOpcion no valida. Intente nuevamente.")
