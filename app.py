import tkinter as tk
from tkinter import messagebox
from productos.producto import ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException, Producto
from tienda.tienda import Tienda

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Registro de Productos")
        
        self.tienda = Tienda()
        
        # Etiquetas y entradas para agregar un producto
        tk.Label(ventana, text="Nombre del Producto:", bg="sky blue", font=("Arial", 10), bd=1, relief="solid").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(ventana, font=("Arial", 10), bd=1, relief="solid")
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Precio:", bg="sky blue", font=("Arial", 10), bd=1, relief="solid").grid(row=1, column=0, padx=10, pady=5)
        self.precio_entry = tk.Entry(ventana, font=("Arial", 10), bd=1, relief="solid")
        self.precio_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Cantidad:", bg="sky blue", font=("Arial", 10), bd=1, relief="solid").grid(row=2, column=0, padx=10, pady=5)
        self.cantidad_entry = tk.Entry(ventana, font=("Arial", 10), bd=1, relief="solid")
        self.cantidad_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Botones para agregar y mostrar productos
        tk.Button(ventana, text="Agregar Producto", bg="blue", fg="white", font=("Arial", 12), command=self.agregar_producto).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(ventana, text="Mostrar Detalles", bg="blue", fg="white", font=("Arial", 12), command=self.mostrar_detalles).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Área de entrada para modificar inventario
        tk.Label(ventana, text="Nombre del Producto:", bg="sky blue", font=("Arial", 10), bd=1, relief="solid").grid(row=5, column=0, padx=10, pady=5)
        self.nombre_modificar_entry = tk.Entry(ventana, font=("Arial", 10), bd=1, relief="solid")
        self.nombre_modificar_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(ventana, text="Cantidad a Agregar/Quitar:", bg="sky blue", font=("Arial", 10), bd=1, relief="solid").grid(row=6, column=0, padx=10, pady=5)
        self.cantidad_modificar_entry = tk.Entry(ventana, font=("Arial", 10), bd=1, relief="solid")
        self.cantidad_modificar_entry.grid(row=6, column=1, padx=10, pady=5)
        
        # Botón para modificar inventario
        tk.Button(ventana, text="Modificar Inventario", bg="blue", fg="white", font=("Arial", 12), command=self.modificar_inventario).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Área de salida
        self.output_text = tk.Text(ventana, height=10, width=40, font=("Arial", 10), bd=1, relief="solid")
        self.output_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        
    def agregar_producto(self):
        """Agrega un producto a la tienda."""
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            
            producto = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
            self.tienda.registrar_producto(producto)
            
            messagebox.showinfo("Éxito", "Producto registrado con éxito")
            self.limpiar_entradas()
            
        except (ProductoInvalidoException, PrecioInvalidoException, CantidadInvalidaException) as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser numéricos")
    
    def mostrar_detalles(self):
        """Muestra detalles de todos los productos registrados."""
        self.output_text.delete(1.0, tk.END)
        
        if not self.tienda.lista_productos:
            self.output_text.insert(tk.END, "No hay productos registrados\n")
        else:
            for producto in self.tienda.lista_productos:
                detalles = (f"Nombre: {producto.nombre}\n"
                            f"Precio: {producto.precio}\n"
                            f"Cantidad: {producto.cantidad}\n"
                            f"Valor Total: {producto.calcular_valor_total()}\n\n")
                self.output_text.insert(tk.END, detalles)
    
    def modificar_inventario(self):
        """Modifica el inventario de un producto específico."""
        nombre = self.nombre_modificar_entry.get()
        try:
            cantidad_modificar = int(self.cantidad_modificar_entry.get())
            
            producto = self.tienda.buscar_producto(nombre)
            if producto:
                producto.modificar_inventario(cantidad_modificar)
                messagebox.showinfo("Éxito", f"Inventario actualizado para '{nombre}'")
                self.mostrar_detalles()
            else:
                messagebox.showerror("Error", "Producto no encontrado")
                
        except CantidadInvalidaException as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Cantidad a modificar debe ser un número entero")
    
    def limpiar_entradas(self):
        """Limpia las entradas de agregar producto."""
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.nombre_modificar_entry.delete(0, tk.END)
        self.cantidad_modificar_entry.delete(0, tk.END)

# ventana = tk.Tk()
# app = App(ventana)
# ventana.mainloop()
 