from paciente.paciente import Paciente
from medico.medico import Medico
from typing import List


class ValidadorHospital:
    
    
    
    def validar_existencia_paciente(self, id_paciente: int, lista_pacientes: List[Paciente]):
        for paciente in lista_pacientes:
            if paciente.id == id_paciente:
                return True
            
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
    
    def validar_cantidad_usuarios(self, lista_pacientes: List[Paciente], lista_medicos: List[Medico]):
        if len(lista_pacientes) == 0:
            print("No existen pacientes, no puedes registrar una consulta")
            return False
        
        if len(lista_medicos) == 0:
            print("No existen medicos, no puedes registrar una consulta")
            return False
        
        return True