
import random

class Paciente:
    id = 0
    nombre = ""
    nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    
    def __init__(self, nombre, nacimiento, peso, estatura, direccion):
        self.id = random.randint(1, 100000)
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("Id: ", self.id)
        print(f"Nombre: {self.nombre}")
        print(f"Año de Nacimiento: {self.nacimiento}")
        print(f"Peso: {self.peso}")
        print(f"Estatura: {self.estatura}")
        print(f"Direccion: {self.direccion}")
    
# @property
# def id(self):
#     return self.id

# @property
# def nombre(self):
#     return self.nombre

# @property
# def nacimiento(self):
#     return self.nacimiento

# @property
# def peso(self):
#     return self.peso

# @property
# def estatura(self):
#     return self.estatura

# @property
# def direccion(self):
#     return self.direccion
 