 
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
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero
        
    def generar_id(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(1, 100000)}-{randint(1, 100000)}"
    
    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)
        
    def mostrar_info_semestre(self):
        info = f"ID: {self.id}, Numero: {self.numero}, ID de la carrera: {self.id_carrera}"
        return info
