class Hospital:
    pacientes = []
    medicos = []
    consultas = []
    
    def registrar_consulta(self, id_paciente, id_medico):
        if self.validar_cantidad_usuarios() == False:
            return

        if self.validar_existencia_paciente() == False or self.validar_existencia_medico() == False:
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
            paciente.mostrar_informacion()
            # if paciente.id == id_paciente:
            #     return True
            
    def mostrar_medicos(self):
        print("*** Médicos en el sistema ***")
        for medico in self.medicos:
            print(f"ID: {medico.id}, Nombre: {medico.nombre}, RFC: {medico.rfc}, Dirección: {medico.direccion}")

    def mostrar_pacientes_menores_edad(self):
        print("*** Pacientes menores de edad ***")
        for paciente in self.pacientes:
            if self.calcular_edad(paciente) < 18:
                paciente.mostrar_informacion()

    def mostrar_pacientes_mayores_edad(self):
        print("*** Pacientes mayores de edad ***")
        for paciente in self.pacientes:
            if self.calcular_edad(paciente) >= 18:
                paciente.mostrar_informacion()

    def eliminar_paciente_por_id(self, id_paciente):
        self.pacientes = [paciente for paciente in self.pacientes if paciente.id != id_paciente]
        print(f"Paciente con ID {id_paciente} ha sido eliminado.")

    def eliminar_medico_por_id(self, id_medico):
        self.medicos = [medico for medico in self.medicos if medico.id != id_medico]
        print(f"Médico con ID {id_medico} ha sido eliminado.")
    
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
            
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No existen pacientes, no puedes registrar una consulta")
            return False
        
        if len(self.medicos) == 0:
            print("No existen medicos, no puedes registrar una consulta")
            return False
        
        return True
    
    def calcular_edad(self, persona):
        from datetime import datetime
        return datetime.now().year - persona.nacimiento
 