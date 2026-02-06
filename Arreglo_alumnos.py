import random

def main():
    # --- 1. CONFIGURACIÓN ---
    FILAS_ALUMNOS = 500
    COLUMNAS_MATERIAS = 6
    
    matriz = []

    # Llenamos la matriz
    for i in range(FILAS_ALUMNOS):
        calificaciones = [random.randint(60, 100) for _ in range(COLUMNAS_MATERIAS)]
        matriz.append(calificaciones)

    # --- 2. IMPRESIÓN DE LA TABLA (Visualización) ---
    print("\n--- TABLA DE CALIFICACIONES (Parcial) ---\n")
    
    header = f"{'ALUMNO':<12} |"
    for m in range(COLUMNAS_MATERIAS):
        header += f" {'MAT ' + str(m):<7} |"
    
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    # Imprimimos los 500 alumnos
    for i in range(FILAS_ALUMNOS):
        fila_str = f"{'Alumno ' + str(i):<12} |"
        for nota in matriz[i]:
            fila_str += f" {nota:<7} |"
        print(fila_str)

    print("-" * len(header)) 

    # --- 3. BÚSQUEDA INTERACTIVA (Nueva función) ---
    print("\n" + "="*40)
    print("       BÚSQUEDA DE CALIFICACIONES")
    print("="*40)

    try:
        # Solicitamos los datos al usuario
        # int() convierte el texto que escribes en un número entero
        input_alumno = int(input(f"Ingrese el número del Alumno (0 - {FILAS_ALUMNOS - 1}): "))
        input_materia = int(input(f"Ingrese el número de la Materia (0 - {COLUMNAS_MATERIAS - 1}): "))

        # Validamos que los números existan en nuestra matriz
        if (0 <= input_alumno < FILAS_ALUMNOS) and (0 <= input_materia < COLUMNAS_MATERIAS):
            
            # Buscamos el dato
            nota_encontrada = matriz[input_alumno][input_materia]
            
            print(f"\n✅ RESULTADO:")
            print(f"El Alumno {input_alumno} tiene una nota de {nota_encontrada} en la Materia {input_materia}.")
            
        else:
            print(f"\n❌ ERROR: Los números deben estar dentro del rango.")
            print(f"   Alumno debe ser entre 0 y {FILAS_ALUMNOS - 1}")
            print(f"   Materia debe ser entre 0 y {COLUMNAS_MATERIAS - 1}")

    except ValueError:
        print("\n❌ ERROR: Por favor, ingrese solamente números enteros.")

if __name__ == "__main__":
    main()