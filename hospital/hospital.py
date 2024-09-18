
from typing import List
from paciente.paciente import Paciente
from medico.medico import Medico
from consulta.consulta import Consulta
from validador_hospital import ValidadorHospital

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []
    validador_hospital = ValidadorHospital()

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validador_hospital.validar_cantidad_usuarios(lista_pacientes=self.pacientes, lista_medicos=self.medicos):
            return

        if not self.validador_hospital.validar_existencia_paciente(id_paciente=id_paciente, lista_pacientes=self.pacientes):
            print("Nos se puede registrar la consulta, no hay medicos o pacientes")
            return
        
        print("Continuamos con el registro")
        
    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
        # print("Validacion exitosa")
        
    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def mostrar_pacientes(self):
        print("*** Pacientes en el sistema ***")
        for paciente in self.pacientes:
            print("------------------------------------------------------")
            paciente.mostrar_informacion()
            # if paciente.id == id_paciente:
            #     return True
            
    def mostrar_medicos(self):
        print("------------------------------------------------------")
        print("*** Médicos en el sistema ***")
        for medico in self.medicos:
            print(f"ID: {medico.id}")
            print(f"Nombre: {medico.nombre}")
            print(f"RFC: {medico.rfc}")
            print(f"Dirección: {medico.direccion}")

    def mostrar_pacientes_menores_edad(self):
        print("*** Pacientes menores de edad ***")
        for paciente in self.pacientes:
            if self.calcular_edad(paciente) < 18:
                print("------------------------------------------------------")
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores_edad(self):
        print("*** Pacientes mayores de edad ***")
        for paciente in self.pacientes:
            if self.calcular_edad(paciente) >= 18:
                print("------------------------------------------------------")
                paciente.mostrar_informacion()

    def eliminar_paciente_por_id(self, id_paciente):
        self.pacientes = [paciente for paciente in self.pacientes if paciente.id != id_paciente]
        print(f"Paciente con ID {id_paciente} ha sido eliminado.")

    def eliminar_medico_por_id(self, id_medico):
        self.medicos = [medico for medico in self.medicos if medico.id != id_medico]
        print(f"Médico con ID {id_medico} ha sido eliminado.")
    
    def calcular_edad(self, persona):
        from datetime import datetime
        return datetime.now().year - persona.nacimiento
 