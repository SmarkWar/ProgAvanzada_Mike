
import random

class Medico:
    id = 0
    nombre = ""
    nacimiento = 0
    rfc = ""
    direccion = ""
    
    def __init__(self, nombre, nacimiento, rfc, direccion):
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
 