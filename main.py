
"""
- Pacientes
- Medicos
- Habitaciones
- Consultas
- Medicamentos
    
"""

from paciente.paciente import Paciente
from hospital.hospital import Hospital
from medico.medico import Medico

hospital = Hospital()

# while True:
#     print("BIENVENIDO AL SISTEMA DEL HOSPITAL")
#     print("1. Registrar Paciente")
#     print("2. Registrar Medico")
#     print("3. Mostrar Pacientes")
#     print("4. Mostrar Medicos")
#     print("5. Eliminar Pacientes")
#     print("6. Eliminar Medicos")
#     print("7. Mostrar Pacientes menores de edad")
#     print("8. Mostrar Pacientes mayores de edad")
#     print("9. Salir")
    
#     opcion_usuario = input("Selecciona la opcion deseada: ")
    
#     if opcion_usuario == "1":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para registrar un paciente")
        
#         nombre = input("Ingresa el nombre: ")
#         nacimiento = int(input("Ingresa el año de naciemiento: "))
#         peso = float(input("Ingresa el peso: "))
#         estatura = float(input("Ingresa la estatura: "))
#         direccion = input("Ingresa la direccion: ")
        
#         paciente = Paciente(nombre=nombre, nacimiento=nacimiento, peso=peso, estatura=estatura, direccion=direccion)
#         hospital.registrar_paciente(paciente=paciente)
#         print("Paciente registrado correctamente")
#         print("------------------------------------------------------")
        
#     elif opcion_usuario == "2":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para registrar un medico")
        
#         nombre = input("Ingresa el nombre: ")
#         nacimiento = int(input("Ingresa el año de naciemiento: "))
#         rfc = input("Ingresa el RFC: ")
#         direccion = input("Ingresa la direccion: ")
        
#         medico = Medico(nombre=nombre, nacimiento=nacimiento, rfc=rfc, direccion=direccion)
#         hospital.registrar_medico(medico=medico)
        
#         print("Medico registrado correctamente")
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "3":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para ver los pacientes")
#         hospital.mostrar_pacientes()
#         print("------------------------------------------------------")
        
#     elif opcion_usuario == "4":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para ver los medicos")
#         hospital.mostrar_medicos()
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "5":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opción para eliminar un paciente")
#         id_paciente = int(input("Ingresa el ID del paciente a eliminar: "))
#         hospital.eliminar_paciente_por_id(id_paciente)
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "6":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para eliminar un medico")
#         id_medico = int(input("Ingresa el ID del medico a eliminar: "))
#         hospital.eliminar_medico_por_id(id_medico)
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "7":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para mostrar pacientes menores de edad")
#         hospital.mostrar_pacientes_menores_edad()
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "8":
#         print("------------------------------------------------------")
#         print("Seleccionaste la opcion para mostrar pacientes mayores de edad")
#         hospital.mostrar_pacientes_mayores_edad()
#         print("------------------------------------------------------")
    
#     elif opcion_usuario == "9":
#         print("------------------------------------------------------")
#         print("Hasta Luego")
#         break

# paciente= Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
# paciente_dos= Paciente("Jonathan", 2005, 70, 1.90, "Circuito")

# medico = Medico("Alberto", 1900, "COCM040323IJ7",  "Av. Periodismo")

# hospital.registrar_paciente(paciente=paciente)
# hospital.registrar_paciente(paciente=paciente_dos)

# hospital.registrar_medico(medico=medico)

# hospital.mostrar_pacientes()
    