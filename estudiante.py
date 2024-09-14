from curso import Curso

class Estudiante:
    
    def __init__(self, nombre, edad, id_estudiante, curso):
        self.nombre = nombre
        self.edad = edad
        self.id_estudiante = id_estudiante
        self.cursos = []
        
    def agregar_curso(self, curso):
        self.cursos.append(curso)
        print("Nuevo curso agregado")
        
    def mostrar_info_estudiante(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nID del Estudiante: ", self.id_estudiante)
        
        if self.cursos:
            print("Cursos: ")
            for curso in self.cursos:
                curso.mostrar_info_curso()
                
        else:
            print("No tiene cursos asignados para mostrar")

