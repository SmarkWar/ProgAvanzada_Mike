 
from typing import List
from materias.materia import Materia
from estudiantes.estudiante import Estudiante
from semestre.semestre import Semestre

class Carrera:
    matricula: str
    nombre: str
    materias: List[Materia] = []
    numero_semestre: int
    estudiante: List[Estudiante] = []
    semestres: List[Semestre] = []
 