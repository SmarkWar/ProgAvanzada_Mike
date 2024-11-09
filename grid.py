import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text = "Etiqueta 1")
label1.grid(row = 0, column = 1)

label2 = tk.Label(root, text = "Etiqueta 2")
label2.grid(row = 0, column = 0)

root.mainloop()
