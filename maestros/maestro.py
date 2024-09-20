
from datetime import datetime

class Maestro:
    numero_control_maestro: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    ano_nacimiento: datetime
    
    def __init__(self, numero_control_maestro: str, rfc: str, nombre: str, apellido: str, sueldo: float, ano_nacimiento: datetime):
        self.numero_control_maestro = numero_control_maestro
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
        self.ano_nacimiento = ano_nacimiento
 