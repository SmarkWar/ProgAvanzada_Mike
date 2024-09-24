 
from datetime import datetime

class Maestro:
    numero_control_maestro: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    fecha_nacimiento_maestro: datetime
    
    def __init__(self, numero_control_maestro: str, rfc: str, nombre: str, apellido: str, sueldo: float, fecha_nacimiento_maestro: datetime):
        self.numero_control_maestro = numero_control_maestro
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_nacimiento_maestro = fecha_nacimiento_maestro
        

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.numero_control_maestro}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}, Fecha de nacimiento: {self.fecha_nacimiento_maestro}"
        return info
 