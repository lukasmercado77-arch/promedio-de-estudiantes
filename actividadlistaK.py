def registro_procedural():
  print("=== MÉTODO 1: Enfoque Procedural ===")
  estudiantes = []

  while True:
    nombre = input(
        "Ingresa el nombre del estudiante (o escribe 'salir' para terminar): "
    )
    if nombre.lower() == "salir":
      break

    try:
      nota = float(input(f"Ingresa la nota de {nombre}: "))
      estudiantes.append({"nombre": nombre, "nota": nota})
    except ValueError:
      print("Error: La nota debe ser un número válido.\n")

  
  print("\n--- Lista de Estudiantes y Notas ---")
  if not estudiantes:
    print("No se registraron estudiantes.")
  else:
    for est in estudiantes:
      print(f"• Estudiante: {est['nombre']} | Nota: {est['nota']}")



registro_procedural()