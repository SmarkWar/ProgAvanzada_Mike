 
from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    id_carrera: str
    metrias: List[Materia] = []
    grupos: List[Grupo] = []
    
    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id()
        self.id_carrera = id_carrera
        
    def generar_id(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(1, 100000)}-{randint(1, 100000)}"
 