class RepositorioDatos:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []
        self.matriculas = []

    # --- Estudiantes ---
    def guardar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, identificacion):
        for e in self.estudiantes:
            if e["identificacion"] == identificacion:
                return e
        return None

    def listar_estudiantes(self):
        return self.estudiantes

    # --- Cursos ---
    def guardar_curso(self, curso):
        self.cursos.append(curso)

    def buscar_curso(self, codigo):
        for c in self.cursos:
            if c["codigo"] == codigo:
                return c
        return None

    def listar_cursos(self):
        return self.cursos

    # --- Matrículas ---
    def guardar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def matricula_existente(self, identificacion, codigo_curso):
        return any(
            m["identificacion"] == identificacion and m["codigo_curso"] == codigo_curso
            for m in self.matriculas
        )

    def listar_matriculas(self):
        return self.matriculas
