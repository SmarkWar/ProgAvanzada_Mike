
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    antiguedad: int
    
    def __init__(self, numero_control: str, nombre: str, apellido: str, sueldo: float, rfc: str, antiguedad: int, contrasena: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasena=contrasena, rol=Rol.COORDINADOR)
        self.sueldo = sueldo
        self.rfc = rfc
        self.antiguedad = antiguedad
        
    def mostrar_info_coordinador(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, Sueldo: {self.sueldo}, RFC: {self.rfc}, Años de Antiguedad: {self.antiguedad}, Rol: {self.rol}"
        return info