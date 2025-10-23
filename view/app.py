from controller.negocio import SistemaAcademico

def menu():
    sistema = SistemaAcademico()

    while True:
        print("\n--- SISTEMA ACADÉMICO ---")
        print("1. Registrar estudiante")
        print("2. Registrar curso")
        print("3. Matricular estudiante")
        print("4. Listar estudiantes")
        print("5. Listar cursos")
        print("6. Listar matrículas")
        print("7. Buscar estudiante")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            identificacion = input("Identificación: ")
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            sistema.registrar_estudiante(nombre, identificacion, carrera, semestre)

        elif opcion == "2":
            codigo = input("Código del curso: ")
            nombre = input("Nombre del curso: ")
            creditos = int(input("Créditos: "))
            sistema.registrar_curso(codigo, nombre, creditos)

        elif opcion == "3":
            id_est = input("Identificación del estudiante: ")
            cod_curso = input("Código del curso: ")
            sistema.matricular_estudiante(id_est, cod_curso)

        elif opcion == "4":
            sistema.listar_estudiantes()

        elif opcion == "5":
            sistema.listar_cursos()

        elif opcion == "6":
            sistema.listar_matriculas()

        elif opcion == "7":
            identificacion = input("Identificación: ")
            sistema.buscar_estudiante(identificacion)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
