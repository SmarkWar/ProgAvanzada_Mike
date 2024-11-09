import tkinter as tk
 
def cambiar_texto():
    etiqueta.config(text="¡Texto actualizado!")
 
ventana = tk.Tk()
ventana.title("Ejemplo de atributos")
 
etiqueta = tk.Label(ventana, text="Hola, Tkinter!", bg="lightgreen", fg="black", font=("Arial", 16, "bold"), relief="sunken", padx=10, pady=10)
etiqueta.pack(padx=20, pady=20)
 
boton = tk.Button(ventana, text="Actualizar texto", bg="blue", fg="white", font=("Arial", 12), command=cambiar_texto)
boton.pack(pady=10)
 
entrada = tk.Entry(ventana, font=("Arial", 14), bd=2, relief="solid")
entrada.pack(pady=10)
 
ventana.mainloop()