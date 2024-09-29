 
from datetime import datetime
from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from semestre.semestre import Semestre

escuela = Escuela()

while True:
    print("----------------------------------------------------")
    print("** MindBox **")
    print("1. Registrar Estudiante")
    print("2. Registrar Maestro")
    print("3. Registrar Materia")
    print("4. Registrar Grupo")
    print("5. Registrar Horario")
    print("6. Mostrar Estudiantes")
    print("7. Mostrar Mestros")
    print("8. Mostrar Materias")
    print("9. Mostrar Grupos")
    print("10. Eliminar Estudiante")
    print("11. Eliminar Mestro")
    print("12. Eliminar Materia")
    print("13. Registrar Carrera")
    print("14. Registrar Semestre")
    print("15. Mostrar Carrera")
    print("16. Mostrar Semestre")
    print("17. Mostrar Grupo")
    print("18. Salir")
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
        
        numero_control = escuela.generar_numero_control()
        print("Numero de control: ", numero_control)
        estudiante = Estudiante("", nombre, apellido, curp, fecha_nacimiento)
        estudiante.numero_control = numero_control
        escuela.registrar_estudiante(estudiante)
        
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
    
        maestro = Maestro("", rfc, nombre, apellido, sueldo, fecha_nacimiento_maestro)
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
        print("----------------------------------------------------")
        print("Elegiste la opcion para registrar un nuevo grupo")
        print("----------------------------------------------------")
        tipo = input("Ingresa el tipo de grupo (A o B): ")
        id_semestre = input("Ingresa el ID del semestre al que pertenece: ")
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        escuela.registrar_grupo(grupo=grupo)
    
    if opcion == "5":
        pass
    
    if opcion == "6":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar los estudiantes")
        print("----------------------------------------------------")
        escuela.listar_estudiantes()
        
    if opcion == "7":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar los maestros")
        print("----------------------------------------------------")
        escuela.listar_maestros()
    
    if opcion == "8":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar las materias")
        print("----------------------------------------------------")
        escuela.listar_materias()
    
    if opcion == "9":
        pass
    
    if opcion == "10":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para eliinar un estudiante")
        print("----------------------------------------------------")
        numero_control = input("Ingresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control)
    
    if opcion == "11":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para eliinar un maestro")
        print("----------------------------------------------------")
        numero_control_maestro = input("Ingresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control_maestro)
    
    if opcion == "12":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para eliinar una materia")
        print("----------------------------------------------------")
        numero_control_materia = input("Ingresa el numero de control de la materia: ")
        escuela.eliminar_materia(numero_control_materia)
    
    if opcion == "13":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para registrar una carrera")
        print("----------------------------------------------------")
        nombre = input("Ingresa el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre)
        escuela.registrar_carrera(carrera=carrera)
        
    if opcion == "14":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para registrar un semestre")
        print("----------------------------------------------------")
        numero = input("Ingresa el numero del semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: ")
        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        escuela.registrar_semestre(semestre=semestre)
    
    if opcion == "15":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar las carreras")
        print("----------------------------------------------------")
        escuela.listar_carreras()
        
    if opcion == "16":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar los semestres")
        print("----------------------------------------------------")
        escuela.listar_semestres()
        
    if opcion == "17":
        print("----------------------------------------------------")
        print("Seleccionaste la opcion para mostrar los grups")
        print("----------------------------------------------------")
        escuela.listar_grupos()
    
    if opcion == "18":
        print("----------------------------------------------------")
        print("Hasta luego")
        break
 