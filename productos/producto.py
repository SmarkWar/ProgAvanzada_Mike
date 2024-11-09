from excepciones.excepciones import PrecioInvalidoException, CantidadInvalidaException, ProductoInvalidoException

class Producto():
    nombre: str
    precio: float
    cantidad: int
    
    def __init__(self, nombre: str, precio: float, cantidad: int):
        
        if not nombre:
            raise ProductoInvalidoException()
        if precio <= 0:
            raise PrecioInvalidoException()
        if cantidad < 0:
            raise CantidadInvalidaException()
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def calcular_valor_total(self):
        return self.precio * self.cantidad
      
    def mostrar_detalles(self):
        valor_total = self.calcular_valor_total()
        print(f"Nombre: {self.nombre}, \nPrecio Individual: {self.precio}, \nProductos en Existencia: {self.cantidad}, \nValor total de los Productos: {valor_total}")

    def modificar_inventario(self, cantidad: int):
        """Modifica el inventario sumando o restando la cantidad especificada."""
        nueva_cantidad = self.cantidad + cantidad
        
        if nueva_cantidad < 0:
            raise CantidadInvalidaException("No se puede reducir el inventario por debajo de cero")
        
        self.cantidad = nueva_cantidad
        operacion = "agregado" if cantidad > 0 else "quitado"
        print(f"Se ha {operacion} {abs(cantidad)} unidades al inventario. Nueva cantidad: {self.cantidad}")
 