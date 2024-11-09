
from productos.producto import  Producto
from typing import List, Optional

class Tienda():
    lista_productos: List[Producto] = []
    
    def registrar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        print("Se registro el producto con exito")
        
    def listar_productos(self):
        for producto in self.lista_productos:
            print(producto.mostrar_detalles())

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """Busca un producto por nombre en la lista de productos."""
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        print("Producto no encontrado.")
        return None