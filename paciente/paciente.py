
import random



class Paciente:
    id: int
    nombre: str
    nacimiento: int
    peso: float
    estatura: float
    direccion: str
    
    def __init__(self, nombre: str, nacimiento: int, peso: float, estatura: float, direccion: str):
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
 