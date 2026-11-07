
# ==========================================
# SISTEMA DE GESTION DE CALIFICACIONES
# ==========================================

estudiantes = [
    {"nombre": "Lucas", "nota": 3.5},
    {"nombre": "Bob", "nota": 4.0},
    {"nombre": "Carlos", "nota": 2.5},
    {"nombre": "Maria", "nota": 5.0},
    {"nombre": "Daniel", "nota": 1.5},
    {"nombre": "Ana", "nota": 4.8}
]

# Variables de control
aprobados = []
reprobados = []
notas_invalidas = []

# Funcion para evaluar notas
def evaluar_nota(nota):

    if not isinstance(nota, (int, float)):
        return "Error: la nota debe ser numerica"

    elif nota < 0 or nota > 5:
        return "Nota invalida"

    elif nota >= 3:
        return "Aprobado"

    else:
        return "Reprobado"


# Recorrer todos los estudiantes
for estudiante in estudiantes:

    nombre = estudiante.get("nombre", "Desconocido")
    nota = estudiante.get("nota")

    resultado = evaluar_nota(nota)

    print("\n-------------------------")
    print("Estudiante:", nombre)
    print("Calificacion:", nota)
    print("Resultado:", resultado)

    # Clasificar estudiantes
    if resultado == "Aprobado":
        aprobados.append(estudiante)

    elif resultado == "Reprobado":
        reprobados.append(estudiante)

    else:
        notas_invalidas.append(estudiante)


# Calcular estadisticas
notas_validas = [
    e["nota"] for e in estudiantes
    if isinstance(e.get("nota"), (int, float))
    and 0 <= e["nota"] <= 5
]

if notas_validas:

    promedio = sum(notas_validas) / len(notas_validas)

    nota_mayor = max(notas_validas)
    nota_menor = min(notas_validas)

else:
    promedio = 0
    nota_mayor = 0
    nota_menor = 0


# Informe final
print("\n========== INFORME FINAL ==========")

print("Total de estudiantes:", len(estudiantes))
print("Aprobados:", len(aprobados))
print("Reprobados:", len(reprobados))
print("Notas invalidas:", len(notas_invalidas))

print("Promedio general:", round(promedio, 2))
print("Nota mas alta:", nota_mayor)
print("Nota mas baja:", nota_menor)

print("\nEstudiantes aprobados:")

for estudiante in aprobados:
    print("-", estudiante["nombre"])

print("\nEstudiantes reprobados:")

for estudiante in reprobados:
    print("-", estudiante["nombre"])
