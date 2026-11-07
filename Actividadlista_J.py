def gestionar_calificaciones():
  print("=== MÉTODO 1 (Versión Alternativa Procedural) ===")
  coleccion_alumnos = []

  while True:
    etiqueta_nombre = input(
        "Introduce el nombre del alumno (escribe 'parar' para concluir): "
    )
    if etiqueta_nombre.lower() == "parar":
      break

    try:
      calificacion = float(
          input(f"Introduce la calificación para {etiqueta_nombre}: ")
      )
      coleccion_alumnos.append(
          {"alumno": etiqueta_nombre, "calificacion": calificacion}
      )
    except ValueError:
      print("Aviso: Debe ingresar un valor numérico válido.\n")
  print("\n--- Registro de Alumnos y Calificaciones ---")
  if not coleccion_alumnos:
    print("No existen registros guardados.")
  else:
    for item in coleccion_alumnos:
      print(
          f"-> Alumno/a: {item['alumno']} | Calificación:"
          f" {item['calificacion']}"
      )

gestionar_calificaciones()