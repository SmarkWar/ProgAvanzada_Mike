 
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
        numero_control_maestro = f"M{maestro.fecha_nacimiento_maestro.year}{datetime.now().day}{randint(500, 5000)}{maestro.nombre[:2].upper()}{maestro.rfc[-2:].upper()}{len(self.lista_maestros)+1}"
        return numero_control_maestro
    
    def registrar_materia(self, materia:Materia):
        self.lista_materias.append(materia)
        
    def generar_numero_control_materia(self, materia: Materia, semestre: Materia, creditos: Materia):
        # "MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{random 1, 1000}"
        numero_control_materia = f"MT{materia.nombre[-2:].upper()}{semestre}{creditos}{randint(1, 1000)}"
        return numero_control_materia
    
    def listar_estudiantes(self):
        print("----------------------------------------------------")
        print("** ESTUDIANTES **")
        
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
    
    def eliminar_estudiante(self, numero_control: str):
        print("----------------------------------------------------")
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        
        print(f"No se encontro el estudiante con numero de control: {numero_control}")
        
    def listar_maestros(self):
        print("----------------------------------------------------")
        print("** MAESTROS **")
        
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
    
    def eliminar_maestro(self, numero_control_maestro: str):
        print("----------------------------------------------------")
        for maestro in self.lista_maestros:
            if maestro.numero_control_maestro == numero_control_maestro:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        
        print(f"No se encontro el maestro con numero de control: {numero_control_maestro}")
 
    def listar_materias(self):
        print("** MATERIAS **")
        
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
    
    def eliminar_materia(self, numero_control_materia: str):
        for materia in self.lista_materias:
            if materia.numero_control_materia == numero_control_materia:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        
        print(f"No se encontro la materia con numero de control: {numero_control_materia}")
 