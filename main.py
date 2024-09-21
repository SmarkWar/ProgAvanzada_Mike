
from datetime import datetime
from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia

escuela = Escuela()

while True:
    print("----------------------------------------------------")
    print("** MindBox **")
    print("1. Registrar Estudiante")
    print("2. Registrar Maestro")
    print("3. Registrar Materia")
    print("4. Registrar Grupo")
    print("5. Registrar Horario")
    print("6. Registrar Horario")
    print("----------------------------------------------------")
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("----------------------------------------------------")
        print("Elegiste la opcion para registrar un estudiante")
        print("----------------------------------------------------")
        
        numero_control = escuela.generar_numero_control()
        print("Numero de control: ", numero_control)
        
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
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
        fecha_nacimiento = datetime(ano, mes, dia)
    
        maestro = Maestro("", rfc, nombre, apellido, sueldo, fecha_nacimiento)
        numero_control_maestro = escuela.generar_numero_control_maestro(maestro)
        maestro.numero_control_maestro = numero_control_maestro
        escuela.registrar_maestro(maestro)
        
        print("Numero de control: ", numero_control_maestro)
        
    if opcion == "3":
        print("----------------------------------------------------")
        print("Elegiste la opcion para registrar una materia")
        print("----------------------------------------------------")
        
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa una descripcion de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa los creditos correspondientes de la materia: "))

        materia = Materia("", nombre, descripcion, semestre, creditos)
        numero_control_materia = escuela.generar_numero_control_materia(materia, semestre, creditos)
        materia.numero_control_materia = numero_control_materia
        escuela.registrar_materia(materia)
        
        print("Numero de control: ", numero_control_materia)
    
    if opcion == "4":
        pass
    
    if opcion == "5":
        pass
    
    if opcion == "6":
        print("----------------------------------------------------")
        print("Hasta luego")
        break
 