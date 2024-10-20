from maestros.maestro import Maestro
 
class Materia:
    numero_control: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    maestro: Maestro
    
    def __init__(self, numero_control: str, nombre: str, descripcion: str, semestre: int, creditos: int, maestro: Maestro):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.maestro = maestro
        
    def mostrar_info_materia(self):
        info = f"Numero de control: {self.numero_control}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditos}, Maestro: {self.maestro.nombre}"
        return info
 