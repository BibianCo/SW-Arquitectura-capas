from persistence.datos import RepositorioDatos

class SistemaAcademico:
    def __init__(self):
        self.repo = RepositorioDatos()

    def registrar_estudiante(self, nombre, identificacion, carrera, semestre):
        if self.repo.buscar_estudiante(identificacion):
            print("❌ El estudiante ya existe.")
        else:
            self.repo.guardar_estudiante({
                "nombre": nombre,
                "identificacion": identificacion,
                "carrera": carrera,
                "semestre": semestre
            })
            print("✅ Estudiante registrado correctamente.")

    def registrar_curso(self, codigo, nombre, creditos):
        if self.repo.buscar_curso(codigo):
            print("❌ El curso ya existe.")
        else:
            self.repo.guardar_curso({
                "codigo": codigo,
                "nombre": nombre,
                "creditos": creditos
            })
            print("✅ Curso registrado correctamente.")

    def matricular_estudiante(self, identificacion, codigo_curso):
        estudiante = self.repo.buscar_estudiante(identificacion)
        curso = self.repo.buscar_curso(codigo_curso)

        if not estudiante:
            print("❌ Estudiante no encontrado.")
            return
        if not curso:
            print("❌ Curso no encontrado.")
            return
        if self.repo.matricula_existente(identificacion, codigo_curso):
            print("❌ El estudiante ya está matriculado en este curso.")
            return

        self.repo.guardar_matricula({
            "identificacion": identificacion,
            "codigo_curso": codigo_curso
        })
        print("✅ Matrícula registrada correctamente.")

    def listar_estudiantes(self):
        for e in self.repo.listar_estudiantes():
            print(e)

    def listar_cursos(self):
        for c in self.repo.listar_cursos():
            print(c)

    def listar_matriculas(self):
        for m in self.repo.listar_matriculas():
            print(m)

    def buscar_estudiante(self, identificacion):
        e = self.repo.buscar_estudiante(identificacion)
        print(e if e else "No encontrado.")
