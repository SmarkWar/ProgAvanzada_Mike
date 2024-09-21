
class Materia:
    """
    id: "MT{Ultimos dos digitos del nombre}{semestre}{cantidadad creditos}{random(1, 1000)}"
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    """
    numero_control_materia: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__(self, numero_control_materia: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control_materia = numero_control_materia
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
