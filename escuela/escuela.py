
from typing import List
from datetime import datetime
from random import randint
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def generar_numero_control(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0, 10000)
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1, 10000)}"
        return numero_control
    
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)
        
    def generar_numero_control_maestro(self, maestro: Maestro):
        numero_control_maestro = f"M{maestro.ano_nacimiento.year}{datetime.now().day}{randint(500, 5000)}{maestro.nombre[:2].upper()}{maestro.rfc[-2:].upper()}{len(self.lista_maestros)+1}"
        return numero_control_maestro
 
    