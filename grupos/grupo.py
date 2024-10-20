 
from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint

class Grupo:
    id: int
    estudiantes: List[Estudiante] = []
    materias: List[Materia] = []
    tipo: chr
    id_semestre: str
 
    def __init__(self, tipo: chr, id_semestre: str):
        self.id = ""
        self.tipo = tipo
        self.id_semestre = id_semestre
        
    def generar_id(self, tipo: chr) -> str:
        return f"{tipo}-{randint(0, 100000)}-{randint(0, 100000)}"
    
    def mostrar_info_grupo(self):
        info = f"ID: {self.id}, Tipo: {self.tipo}, ID del semestre: {self.id_semestre}"
        return info
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)
        
    def registrar_materia(self, materia: Materia):
        self.materias.append(materia)
        
    def registrar_maestro(self, maestro: Maestro):
        self.maestros.append(maestro)
        
    def mostrar_info_grupo_para_estudiante(self):
        print(f"Informacion del Grupo {self.tipo}, del semestre {self.id_semestre}")
        for materia in self.materias:
            print(materia.mostrar_info_materia())
