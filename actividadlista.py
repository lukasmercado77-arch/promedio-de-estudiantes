
#comensamos con una lista basia
lista_de_estudiantes = []
#Utilizamos while y True para abrir el registro y \n()para organizar mejor
while True:
   print("\n===== MENU PRINCIPAL =====")
   print("1.Registrar estudiante")
   print("2.Finalizar registro")
   opcion = input("Seleccione una opcion:")
# se usa if() para empesar el empesar el registro
   if opcion == "1":
       nombre = input("Nombre del estudiante:")
#usamos try para que el codigo no se rompa y falle y usamos except donde le decimos que hacer si falla
       try:
            Nota_1 = float(input("Nota 1 del estudiante:"))
            Nota_2 = float(input("Nota 2 del estudiante:"))
            Nota_3 = float(input("Nota 3 del estudiante:"))

       except ValueError:
           print("Nota invalida, intente de nuevo.")
           continue
#se crea un diccionario con lo datos de los estudiantes y se agrega a la lista utilizando .append()
       promedio_estudiante = ( Nota_1 + Nota_2 + Nota_3) / 3

       estudiante = {
        "Nombre": nombre, 
        "Nota": Nota_1,
        "Nota": Nota_2,
        "Nota": Nota_3,
        "promedio": promedio_estudiante}
       lista_de_estudiantes.append(estudiante)
       print("Estudiante Registrado correctamente.")
#usamos el elif para finalizar
   elif opcion =="2":
       print("\n===== Resultado Final =====")
#utilizamos el for que hace un recorrido para saber cuantos estudiantes se registraron
#Y el in para saber en que lista se va hacer el recorrido
       ganaron = 0
       perdieron = 0
       for estudiante in lista_de_estudiantes:

         print("\nNombre:", estudiante["Nombre"])
         print("Nota:", estudiante["Nota 1"], "-", "Nota:", estudiante["Nota 2"], "-", "Nota:", estudiante["Nota 3"])
         print("promedio:", round(estudiante["promedio"], 2))
# Evaluamos la variable Nota directamente
         if estudiante ["Nota"] >= 3:
              print("estudiante: GANO")
              ganaron +=1
         else:
              print("estudiante: PERDIO")
              perdieron += 1
               # ===== ESTADISTICAS (fuera del for) =====
         if len(lista_de_estudiantes) > 0:
            promedios = [e["Promedio"] for e in lista_de_estudiantes]

            total = len(promedios)
            promedio_grupo = sum(promedios) / total
            porcentaje_aprobados = (ganaron / total) * 100

            # Lista con TODAS las notas: (nota, nombre, numero de nota)
            todas_las_notas = []
            for e in lista_de_estudiantes:
                for i in (1, 2, 3):
                    todas_las_notas.append((e["Nota " + str(i)], e["Nombre"], i))

            nota_maxima = max(todas_las_notas, key=lambda t: t[0])
            nota_minima = min(todas_las_notas, key=lambda t: t[0])

            print("\n===== ESTADISTICAS =====")
            print("Total de estudiantes:", total)
            print("Promedio del grupo:", round(promedio_grupo, 2))
            print("Nota maxima:", nota_maxima[0], "- sacada por", nota_maxima[1], "(Nota", nota_maxima[2], ")")
            print("Nota minima:", nota_minima[0], "- sacada por", nota_minima[1], "(Nota", nota_minima[2], ")")
            print("Estudiantes que ganaron:", ganaron)
            print("Estudiantes que perdieron:", perdieron)
            print("Porcentaje de aprobacion:", round(porcentaje_aprobados, 1), "%")
         else:
            print("\nNo se registraron estudiantes.")
   else:
      print("\n no se resgistraron estudiantes")
#utilizamos break para finalizar
      print("\nResgistro finalizado.")
      break
else:
       print("opcion no valida")
