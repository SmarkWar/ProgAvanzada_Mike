import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicacion es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("584x200")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="blue", fg="white", font=("Arial", 16, "bold"), relief="sunken", padx=10, pady=10)
label_num1.grid(row = 1, column = 2)
entry_num1 = tk.Entry(ventana, font=("Arial", 14), bd=2, relief="solid")
entry_num1.grid(row = 3, column = 2)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="blue", fg="white", font=("Arial", 16, "bold"), relief="sunken", padx=10, pady=10)
label_num2.grid(row = 1, column = 3)
entry_num2 = tk.Entry(ventana, font=("Arial", 14), bd=2, relief="solid")
entry_num2.grid(row = 3, column = 3)
 
label = tk.Label(text = "")
label.grid(row = 4, column = 0)

label = tk.Label(text = "")
label.grid(row = 2, column = 0)

label = tk.Label(text = "")
label.grid(row = 0, column = 0)
 
boton_sumar = tk.Button(ventana, text="Sumar", bg="blue", fg="white", font=("Arial", 12), command=sumar)
boton_sumar.grid(row = 5, column = 1)

boton_restar = tk.Button(ventana, text="Restar", bg="blue", fg="white", font=("Arial", 12), command=restar)
boton_restar.grid(row = 5, column = 2)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", bg="blue", fg="white", font=("Arial", 12), command=multiplicar)
boton_multiplicar.grid(row = 5, column = 3)

boton_dividir = tk.Button(ventana, text="Dividir", bg="blue", fg="white", font=("Arial", 12), command=dividir)
boton_dividir.grid(row = 5, column = 4)
 
ventana.mainloop()