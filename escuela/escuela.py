 
from typing import List
from random import randint
from datetime import datetime
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from semestre.semestre import Semestre
from usuario.usuario import Usuario
from usuario.utils.roles import Rol
from coordinador.coordinador import Coordinador

class Escuela:
    lista_usuarios: List[Usuario] = []
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []
    lista_coordinadores: List[Coordinador] = []
    
    def __init__(self):
        coordinador = Coordinador(numero_control = "12345", nombre = "Mike", apellido = "Contreras", rfc = "COCM040323IJ7", sueldo = 100000, antiguedad = 10, contrasena = "12345")
        self.lista_usuarios.append(coordinador)
        
    def __init__(self):
        estudiante = Estudiante(numero_control = "123", nombre = "Jose", apellido = "Salazar", curp = "QWERTY12345DFG", fecha_nacimiento = "2004-03-23", contrasena = "123")
        self.lista_usuarios.append(estudiante)
        
    def __init__(self):
        maestro = Maestro(numero_control = "321", nombre = "Roberto", apellido = "Ceballos", rfc = "23456DFGH", sueldo = 40000, fecha_nacimiento_maestro = "2000-03-23", contrasena = "321")
        self.lista_usuarios.append(maestro)
        
    def validar_inicio_sesion(self, numero_control: str, contrasena: str):
        for usuario in self.lista_usuarios:
            if usuario.numero_control == numero_control:
                if usuario.contrasena == contrasena:
                    return usuario
        return None

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_usuarios.append(estudiante)
        self.lista_estudiantes.append(estudiante)
        
    def registrar_maestro(self, maestro: Maestro):
        self.lista_usuarios.append(maestro)
        self.lista_maestros.append(maestro)
    
    def registrar_materia(self, materia:Materia):
        self.lista_materias.append(materia)
    
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
    
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        
        self.lista_grupos.append(grupo)
    
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id
        
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
            
        self.lista_semestres.append(semestre)
        
    def generar_numero_control(self):
        numero_control = f"L{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(1, 10000)}"
        return numero_control
        
    def generar_numero_control_maestro(self, maestro: Maestro):
        numero_control = f"M{maestro.fecha_nacimiento_maestro.year}{datetime.now().day}{randint(500, 5000)}{maestro.nombre[:2].upper()}{maestro.rfc[-2:].upper()}{len(self.lista_maestros)+1}"
        return numero_control
        
    def generar_numero_control_materia(self, materia: Materia, semestre: Materia, creditos: Materia):
        numero_control = f"MT{materia.nombre[-2:].upper()}{semestre}{creditos}{randint(1, 1000)}"
        return numero_control

    def listar_estudiantes(self):
        print("----------------------------------------------------")
        print("** ESTUDIANTES **")
        
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
    
    def mostrar_estudiante(self):
        print("----------------------------------------------------")
        print("*** Mis Datos ***")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante)
        
    def listar_maestros(self):
        print("----------------------------------------------------")
        print("** MAESTROS **")
        
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
    
    def mostrar_maestro(self):
        print("----------------------------------------------------")
        print("*** Mis Datos ***")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro)
            
    def mostrar_coordinador(self):
        print("----------------------------------------------------")
        print("*** Mis Datos ***")
        for coordinador in self.lista_coordinadores:
            print(coordinador.mostrar_info_coordinador)
 
    def listar_materias(self):
        print("----------------------------------------------------")
        print("** MATERIAS **")
        
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
 
    def listar_carreras(self):
        print("----------------------------------------------------")
        print("** CARRERAS **")
        
        for carrera in self.lista_carreras:
            print(carrera.mostrar_info_carrera())
 
    def listar_semestres(self):
        print("----------------------------------------------------")
        print("** SEMESTRES **")
        
        for semestre in self.lista_semestres:
            print(semestre.mostrar_info_semestre())
 
    def listar_grupos(self):
        print("----------------------------------------------------")
        print("** GRUPOS **")
        
        for grupo in self.lista_grupos:
            print(grupo.mostrar_info_grupo())
    
    def eliminar_estudiante(self, numero_control: str):
        print("----------------------------------------------------")
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
        
        print(f"No se encontro el estudiante con numero de control: {numero_control}")
    
    def eliminar_maestro(self, numero_control: str):
        print("----------------------------------------------------")
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("Maestro eliminado")
                return
        
        print(f"No se encontro el maestro con numero de control: {numero_control}")
    
    def eliminar_materia(self, numero_control: str):
        for materia in self.lista_materias:
            if materia.numero_control == numero_control:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
        
        print(f"No se encontro la materia con numero de control: {numero_control}")
    