# view/app.py
from controller.negocio import SistemaAcademico
from persistence.datos import RepositorioDatos
from authentication.seguridad import AuthService

def menu():
    repo = RepositorioDatos()
    sistema = SistemaAcademico(repo)
    auth = AuthService(repo)

    print("=== AUTENTICACIÓN DEL SISTEMA ===")

    while True:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("0. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":  # LOGIN
            username = input("Usuario: ")
            password = input("Contraseña: ")
            if auth.login(username, password):
                print(f" Sesión iniciada como: {username} (Rol: {auth.current_user['rol']})")
                break
            else:
                print("Eroor! Credenciales incorrectas o usuario no existente.")

        elif op == "2":  # REGISTRO
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")

            # Preguntar rol SOLO para creación del primer admin
            print("Rol del usuario:")
            print("1. Administrador")
            print("2. Usuario normal")
            r = input("Seleccione rol: ")
            rol = "admin" if r == "1" else "user"

            try:
                auth.registrar_usuario(username, password, rol)
                print("Usuario creado correctamente. Ahora inicie sesión.")
            except Exception as e:
                print("Error:", e)

        elif op == "0":
            return

        else:
            print("Opción no válida.")

 
    while True:
        print("\n--- SISTEMA ACADÉMICO ---")
        print("1. Registrar estudiante")
        print("2. Registrar curso (solo admin)")
        print("3. Matricular estudiante")
        print("4. Listar estudiantes")
        print("5. Listar cursos")
        print("6. Listar matrículas")
        print("7. Buscar estudiante")
        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            identificacion = input("Identificación: ")
            carrera = input("Carrera: ")
            semestre = int(input("Semestre: "))
            sistema.registrar_estudiante(nombre, identificacion, carrera, semestre)

        elif opcion == "2":
            if not auth.require_role("admin"):
                print("Error! Solo los administradores pueden registrar cursos.")
            else:
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
            auth.logout()
            print("Sesión cerrada.")
            return menu()

        else:
            print("Opción no válida.")
