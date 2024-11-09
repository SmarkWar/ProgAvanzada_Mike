
from productos.producto import Producto
from tienda.tienda import Tienda
from excepciones.excepciones import PrecioInvalidoException, CantidadInvalidaException, ProductoInvalidoException

class Menu():
    
    tienda = Tienda()
    
    def mostrar_menu(self):
        
        while True:
            try:
                print("**** MINISUPER ****")
                print("1. Agregar Producto")
                print("2. Agregar o quitar Existencia de un Producto")
                print("3. Detalles de los Productos")
                print("4. Salir")
                opcion = int(input("Ingresa una opcion: "))
                
                if 1<= opcion <= 4:
                    
                    if opcion == 1:
                        nombre = input("Igresa el nombre del producto: ")
                        precio = float(input("Ingresa el precio del producto: "))
                        cantidad = int(input("Ingresa la cantidad de productos: "))
                        
                        try:
                            producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
                            self.tienda.registrar_producto(producto=producto)
                            
                        except ProductoInvalidoException as e:
                            print(e)
                        except PrecioInvalidoException as e:
                            print(e)
                        except CantidadInvalidaException as e:
                            print(e)
                    
                    elif opcion == 2:
                        nombre = input("Ingresa el nombre del producto a modificar: ")
                        producto = self.tienda.buscar_producto(nombre)
                        
                        if producto:
                            cantidad = int(input("Ingresa la cantidad a modificar (positiva para agregar, negativa para quitar): "))
                            try:
                                producto.modificar_inventario(cantidad)
                            except CantidadInvalidaException as e:
                                print(e)
                        else:
                            print("Producto no encontrado")
                            
                    elif opcion == 3:
                        self.tienda.listar_productos()
                        
                    else:
                        print("Hasta luego")
                        break
                
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 4")
                     
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")
 