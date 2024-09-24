 
class Materia:
    numero_control_materia: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__(self, numero_control_materia: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control_materia = numero_control_materia
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        
    def mostrar_info_materia(self):
        info = f"Numero de control: {self.numero_control_materia}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditos}"
        return info
 