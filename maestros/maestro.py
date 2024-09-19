"""
    numeroControl
    nombre
    apellido
    rfc
    sueldo
"""

class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    
    def __init__(self, nombre: str, apellido: str, sueldo: float):
        self.numero_control = "22L210955"
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = "COCM040323IJ7"
        self.sueldo = sueldo