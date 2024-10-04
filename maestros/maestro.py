 
from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    rfc: str
    sueldo: float
    fecha_nacimiento_maestro: datetime
    
    def __init__(self, numero_control_maestro: str, rfc: str, nombre: str, apellido: str, sueldo: float, fecha_nacimiento_maestro: datetime, contrasena: str):
        super().__init__(numero_control_maestro=numero_control_maestro, nombre=nombre, apellido=apellido, contrasena=contrasena, rol = Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
        self.fecha_nacimiento_maestro = fecha_nacimiento_maestro
        

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Numero de control: {self.numero_control_maestro}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}, Fecha de nacimiento: {self.fecha_nacimiento_maestro}, Rol: {self.rol}"
        return info
 