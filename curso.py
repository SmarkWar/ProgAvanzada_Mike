class Curso:
    
    def __init__(self, nombre_curso, codigo_curso, instructor):
        self.nombre_curso = nombre_curso
        self.codigo_curso = codigo_curso
        self.instructor = instructor

    def mostrar_info_curso(self):
        print("Nombre del curso: ", self.nombre_curso, "\nCodigo del curso: ", self.codigo_curso, "\nInstructor: ", self.instructor)
        return self.mostrar_info_curso

