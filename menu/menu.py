 
from datetime import datetime
from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from semestre.semestre import Semestre
from usuario.utils.roles import Rol
from typing import List
from coordinador.coordinador import Coordinador

class Menu:
    escuela: Escuela = Escuela()
    
    def login(self):
        intentos = 0
        while intentos <5:
            print("----------------------------------------------------")
            print("****** BIENVENIDO ******")
            print("----------------------------------------------------")
            print("Inicia sesion para continuar")
            
            numero_control = input("Ingresa tu numero de control: ")
            contrasena_usuario = input("Ingresa tu contraseña: ")
            
            usuario = self.escuela.validar_inicio_sesion(numero_control=numero_control, contrasena=contrasena_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intentos_sesion_fallido(intentos_usuario = intentos)
            else:
                if usuario.rol == Rol.ESTUDIANTE:
                    self.mostrar_menu_estudainte(usuario)
                    intentos = 0
                elif usuario.rol == Rol.MAESTRO:
                    self.mostrar_menu_maestro(usuario)
                    intentos = 0
                else:
                    self.mostrar_menu(usuario)
                    intentos = 0
                
        print("Maximo de intentos alcanzado, adios")
    
    def mostrar_intentos_sesion_fallido(self, intentos_usuario):
        print("Usuario o contrasena incorrectos, intenta nuevamente")
        return intentos_usuario + 1
    
    def mostrar_menu_estudainte(self, usuario: Estudiante):
        opcion = 0
        while opcion != 4:
            print("----------------------------------------------------")
            print("****** MindBox ******")
            print("1. Ver Horarios")
            print("2. Ver Grupos")
            print("3. Ver mi info")
            print("4. Salir")
            opcion = int(input("Ingresa una opcion: "))
            
            # if opcion == 2:
            #     print("----------------------------------------------------")
            #     print("Seleccionaste la opcion para mostrar los grupos")
            #     print("----------------------------------------------------")
            #     self.escuela.listar_grupos()
            
            if opcion == 3:
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar tu informacion")
                print("----------------------------------------------------")
                print(usuario.mostrar_info_estudiante())
            
            if opcion == 4:
                break
    
    def mostrar_menu_maestro(self, usuario: Maestro):
        opcion = 0
        while opcion != 6:
            print("----------------------------------------------------")
            print("****** MindBox ******")
            print("1. Ver Horarios")
            print("2. Ver Grupos")
            print("3. Ver Materias")
            print("4. Ver Alumnos")
            print("5. Ver mi info")
            print("6. Salir")
            opcion = int(input("Ingresa una opcion: "))
            
            if opcion == 5:
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar tu informacion")
                print("----------------------------------------------------")
                print(usuario.mostrar_info_maestro())
            
            if opcion == 6:
                break
            
    def mostrar_menu(self, usuario: Coordinador):
        while True:
            print("----------------------------------------------------")
            print("** MINDBOX **")
            print("----------------------------------------------------")
            print("1. Registrar Estudiante")
            print("2. Registrar Maestro")
            print("3. Registrar Materia")
            print("4. Registrar Grupo")
            print("5. Registrar Horario")
            print("6. Registrar Carrera")
            print("7. Registrar Semestre")
            print("----------------------------------------------------")
            print("8. Mostrar Estudiantes")
            print("9. Mostrar Mestros")
            print("10. Mostrar Materias")
            print("11. Mostrar Grupos")
            print("12. Mostrar Carrera")
            print("13. Mostrar Semestre")
            print("14. Mostrar Grupo")
            print("----------------------------------------------------")
            print("15. Eliminar Estudiante")
            print("16. Eliminar Mestro")
            print("17. Eliminar Materia")
            print("----------------------------------------------------")
            print("18. Mostrar Info")
            print("19. Salir")
            print("----------------------------------------------------")
            
            opcion = input("Ingresa una opcion para continuar: ")
            
            if opcion == "1":
                print("----------------------------------------------------")
                print("Elegiste la opcion para registrar un estudiante")
                print("----------------------------------------------------")
                
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa la curp del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                
                contrasena = input("Ingresa la contrasena del estudiante: ")
                
                numero_control = self.escuela.generar_numero_control()
                print("Numero de control: ", numero_control)
                estudiante = Estudiante("", nombre, apellido, curp, fecha_nacimiento, contrasena)
                estudiante.numero_control = numero_control
                self.escuela.registrar_estudiante(estudiante)
                
            if opcion == "2":
                print("----------------------------------------------------")
                print("Elegiste la opcion para registrar un maestro")
                print("----------------------------------------------------")
                
                nombre = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ")
                rfc = input("Ingresa el rfc del maestro: ")
                sueldo = input("Ingresa el sueldo del maestro: ")
                ano = int(input("Ingresa el año de nacimiento del maestro: "))
                mes = int(input("Ingresa el mes de nacimiento del maestro: "))
                dia = int(input("Ingresa el dia de nacimiento del maestro: "))
                fecha_nacimiento_maestro = datetime(ano, mes, dia)
                
                contrasena = input("Ingresa la contrasena del maestro: ")
            
                maestro = Maestro("", rfc, nombre, apellido, sueldo, fecha_nacimiento_maestro, contrasena)
                numero_control = self.escuela.generar_numero_control_maestro(maestro)
                maestro.numero_control = numero_control
                self.escuela.registrar_maestro(maestro)
                
                print("Numero de control: ", numero_control)
                
            if opcion == "3":
                print("----------------------------------------------------")
                print("Elegiste la opcion para registrar una materia")
                print("----------------------------------------------------")
                
                nombre = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa una descripcion de la materia: ")
                semestre = int(input("Ingresa el semestre de la materia: "))
                creditos = int(input("Ingresa los creditos correspondientes de la materia: "))

                materia = Materia("", nombre, descripcion, semestre, creditos)
                numero_control = self.escuela.generar_numero_control_materia(materia, semestre, creditos)
                materia.numero_control = numero_control
                self.escuela.registrar_materia(materia)
                
                print("Numero de control: ", numero_control)
            
            if opcion == "4":
                print("----------------------------------------------------")
                print("Elegiste la opcion para registrar un nuevo grupo")
                print("----------------------------------------------------")
                tipo = input("Ingresa el tipo de grupo (A o B): ")
                id_semestre = input("Ingresa el ID del semestre al que pertenece: ")
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                self.escuela.registrar_grupo(grupo=grupo)
            
            if opcion == "5":
                pass
            
            if opcion == "6":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para registrar una carrera")
                print("----------------------------------------------------")
                nombre = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera=carrera)
                
            if opcion == "7":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para registrar un semestre")
                print("----------------------------------------------------")
                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                self.escuela.registrar_semestre(semestre=semestre)
            
            if opcion == "8":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar los estudiantes")
                print("----------------------------------------------------")
                self.escuela.listar_estudiantes()
            
            if opcion == "9":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar los maestros")
                print("----------------------------------------------------")
                self.escuela.listar_maestros()
            
            if opcion == "10":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar las materias")
                print("----------------------------------------------------")
                self.escuela.listar_materias()
            
            if opcion == "11":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar los grupos")
                print("----------------------------------------------------")
                self.escuela.listar_grupos()
            
            if opcion == "12":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar las carreras")
                print("----------------------------------------------------")
                self.escuela.listar_carreras()
                
            if opcion == "13":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar los semestres")
                print("----------------------------------------------------")
                self.escuela.listar_semestres()
                
            if opcion == "14":
                pass
            
            if opcion == "15":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para eliinar un estudiante")
                print("----------------------------------------------------")
                numero_control = input("Ingresa el numero de control del estudiante: ")
                self.escuela.eliminar_estudiante(numero_control)
                
            if opcion == "16":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para eliinar un maestro")
                print("----------------------------------------------------")
                numero_control = input("Ingresa el numero de control del maestro: ")
                self.escuela.eliminar_maestro(numero_control)
                
            if opcion == "17":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para eliinar una materia")
                print("----------------------------------------------------")
                numero_control_materia = input("Ingresa el numero de control de la materia: ")
                self.escuela.eliminar_materia(numero_control_materia)
            
            if opcion == "18":
                print("----------------------------------------------------")
                print("Seleccionaste la opcion para mostrar tu informacion")
                print("----------------------------------------------------")
                print(usuario.mostrar_info_coordinador())
            
            if opcion == "19":
                print("----------------------------------------------------")
                print("Hasta luego")
                break
 