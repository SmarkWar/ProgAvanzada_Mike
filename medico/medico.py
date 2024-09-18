    
import random

class Medico:
    id: int
    nombre: str
    nacimiento: int
    rfc: str
    direccion: str
    
    def __init__(self, nombre: str, nacimiento: int, rfc: str, direccion: str):
        self.id = random.randint(1, 100000)
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.rfc = rfc
        self.direccion = direccion
    
@property
def id(self):
    return self.id

@property
def nombre(self):
    return self.nombre

@property
def nacimiento(self):
    return self.nacimiento

@property
def rfc(self):
    return self.rfc

@property
def direccion(self):
    return self.direccion
 