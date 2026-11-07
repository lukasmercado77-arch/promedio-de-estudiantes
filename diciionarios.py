lista_de_estudiantes = []

for i in range(5):
    print("Registro de estudiantes:")
    Nombre = input("Ingrese el Nombre del estudiante: ")
    Nota = float(input("Ingrese la Nota del estudiante: "))
    
    # Evaluamos la variable Nota directamente
    if Nota >= 3:
        estado = "GANO"
    else:
        estado = "PERDIO"
        
    # Creamos el diccionario con los datos de este estudiante
    estudiante = {
        "Nombre": Nombre, 
        "Nota": Nota, 
        "estado": estado
    }
    
    # Agregamos el diccionario a la lista
    lista_de_estudiantes.append(estudiante)

print("\nLista de estudiantes:")
for estudiante in lista_de_estudiantes:
    print(f"estudiante: {estudiante['Nombre']} - Nota: {estudiante['Nota']} - resultado: {estudiante['estado']}")
 