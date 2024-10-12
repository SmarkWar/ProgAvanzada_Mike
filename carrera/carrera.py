 
from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre
from random import randint

class Carrera:
    matricula: str
    nombre: str
    numero_semestre: int = 0
    semestres: List[Semestre] = []
    
    def __init__(self, nombre: str):
        self.matricula = self.generar_id(nombre)
        self.nombre = nombre

    def generar_id(self, nombre: str) -> str:
        return f"{nombre}-{randint(0, 100000)}-{randint(0, 100000)}"
    
    def registrar_semestre(self, semestre: Semestre):
        self.numero_semestre += 1
        self.semestres.append(semestre)
        
    def mostrar_info_carrera(self):
        info = f"Matricula: {self.matricula}, Nombre: {self.nombre}, Numero de semestre: {self.numero_semestre}"
        return info
 