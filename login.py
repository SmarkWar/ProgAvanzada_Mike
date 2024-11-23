
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from tkinter import *

#! VENTANA DEL ADMIN

def mostrar_gestion_empleados():
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Gestion de Empleados")
    
    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select * from usuarios")
        lista = micursos.fetchall() 
        
        for i,(id, nombre, apellido, usuario, contraseña, rol) in enumerate(lista, start = 1):
            listbox.insert("", "end", values = (id, nombre, apellido, usuario, contraseña, rol))
            mysqlC.close()

    def add():
        nombreAdd = name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = role.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"insert into usuarios (id, nombre, apellido, usuario, contraseña, rol) values('{idAdd}','{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraAdd}','{rolAdd}')")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado agregado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"DELETE FROM USUARIOS WHERE id = {idAdd}")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        nombreAdd = name.get()
        apellidoAdd = lastname.get()
        usuarioAdd = user.get()
        contraAdd = password.get()
        rolAdd = role.get()
        idAdd = identificador.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"UPDATE usuarios set nombre = '{nombreAdd}', apellido = '{apellidoAdd}', usuario = '{usuarioAdd}', contraseña = '{contraAdd}', rol = '{rolAdd}' where id = {idAdd}")
            mysqlC.commit()
            name.delete(0, END)
            lastname.delete(0, END)
            user.delete(0, END)
            password.delete(0, END)
            role.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "empleado editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        name.delete(0, END)
        lastname.delete(0, END)
        user.delete(0, END)
        password.delete(0, END)
        role.delete(0, END)
        identificador.delete(0, END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        name.insert(0, seleccion["Nombre"])
        lastname.insert(0, seleccion["Apellido"])
        user.insert(0, seleccion["Usuario"])
        password.insert(0, seleccion["Contraseña"])
        role.insert(0, seleccion["Rol"])
            
    root = tk.Tk()
    root.geometry("1200x600")
    
    label1 = tk.Label(root,text="Registro de empleados", fg="red",font=("Arial",28)).place(x=170,y=0)
    
    global name
    global lastname
    global user
    global password
    global role
    global identificador
    
    labelid = tk.Label(root, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labelnombre = tk.Label(root, text="Nombre", font=("Arial", 12))
    labelnombre.place(x=100, y=80)
    
    labelapellido = tk.Label(root, text="Apellido", font=("Arial", 12))
    labelapellido.place(x=100, y=110)
    
    labelusuario = tk.Label(root, text="Usuario", font=("Arial", 12))
    labelusuario.place(x=100, y=140)
    
    labelcontrasena = tk.Label(root, text="Contraseña", font=("Arial", 12))
    labelcontrasena.place(x=100, y=170)
    
    labelrol = tk.Label(root, text="Rol", font=("Arial", 12))
    labelrol.place(x=100, y=200)
    
    identificador = tk.Entry(root)
    identificador.place(x=270, y=50)
    
    name = tk.Entry(root)
    name.place(x=270, y=80)
    
    lastname = tk.Entry(root)
    lastname.place(x=270, y=110)
    
    user = tk.Entry(root)
    user.place(x=270, y=140)
    
    password = tk.Entry(root)
    password.place(x=270, y=170)
    
    role = tk.Entry(root)
    role.place(x=270, y=200)
    
    tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    
    columnas = ("Id","Nombre","Apellido","Usuario","Contraseña","Rol")
    listbox = ttk.Treeview(root,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtenerR)
    
    root.mainloop()

#! VENTANA DEL EMPLEADO

def mostrar_gestion_libros():
    ventana_sec = tk.Toplevel()
    ventana_sec.title("Gestion de Libros")
    
    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select * from libros")
        lista = micursos.fetchall() 
        
        for i,(id, titulo, autor, editorial, publicacion, precio) in enumerate(lista, start = 1):
            listbox.insert("", "end", values = (id, titulo, autor, editorial, publicacion, precio))
            mysqlC.close()

    def add():
        tituloAdd = title.get()
        autorAdd = writer.get()
        editorialAdd = editorial.get()
        publicacionAdd = publication.get()
        precioAdd = price.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"insert into libros (id, titulo, autor, editorial, publicacion, precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editorialAdd}','{publicacionAdd}','{precioAdd}')")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro agregado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def delete():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"DELETE FROM LIBROS WHERE id = {idAdd}")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro eliminado")
            actualizar()
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        tituloAdd = title.get()
        autorAdd = writer.get()
        editorialAdd = editorial.get()
        publicacionAdd = publication.get()
        precioAdd = price.get()
        idAdd = identificador.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        try:
            micursos.execute(f"UPDATE libros set titulo = '{tituloAdd}', autor = '{autorAdd}', editorial = '{editorialAdd}', publicacion = '{publicacionAdd}', precio = '{precioAdd}' where id = {idAdd}")
            mysqlC.commit()
            title.delete(0, END)
            writer.delete(0, END)
            editorial.delete(0, END)
            publication.delete(0, END)
            price.delete(0, END)
            identificador.delete(0, END)
            messagebox.showinfo("informacion", "libro editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        
    def obtenerR(event):
        title.delete(0, END)
        writer.delete(0, END)
        editorial.delete(0, END)
        publication.delete(0, END)
        price.delete(0, END)
        identificador.delete(0, END)
        
        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0, seleccion["Id"])
        title.insert(0, seleccion["Titulo"])
        writer.insert(0, seleccion["Autor"])
        editorial.insert(0, seleccion["Editorial"])
        publication.insert(0, seleccion["Publicación"])
        price.insert(0, seleccion["Precio"])
    
    def filtrar_por_editorial():
        editorial = entry_editorial.get()
        
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "proyecto")
        micursos = mysqlC.cursor()
        micursos.execute("select editorial * from libros")
        lista = micursos.fetchall() 
        
        for editorial,(id, titulo, autor, editorial, publicacion, precio) in enumerate(lista, start = 1):
            listbox.insert("", "end", values = (id, titulo, autor, editorial, publicacion, precio))
            mysqlC.close()
    
    root = tk.Tk()
    root.geometry("1200x600")
    
    label1 = tk.Label(root,text="Registro de libros", fg="red",font=("Arial",28)).place(x=170,y=0)
    
    global title
    global writer
    global editorial
    global publication
    global price
    global identificador
    
    labelid = tk.Label(root, text="ID", font=("Arial", 12))
    labelid.place(x=100, y=50)
    
    labeltitulo = tk.Label(root, text="Titulo", font=("Arial", 12))
    labeltitulo.place(x=100, y=80)
    
    labelautor = tk.Label(root, text="Autor", font=("Arial", 12))
    labelautor.place(x=100, y=110)
    
    labeleditorial = tk.Label(root, text="Editorial", font=("Arial", 12))
    labeleditorial.place(x=100, y=140)
    
    labelpublicacion = tk.Label(root, text="Publicación", font=("Arial", 12))
    labelpublicacion.place(x=100, y=170)
    
    labelprecio = tk.Label(root, text="Precio", font=("Arial", 12))
    labelprecio.place(x=100, y=200)
    
    labelfiltrareditorial = tk.Label(root, text="Filtrar por Editorial", font=("Arial", 12))
    labelfiltrareditorial.place(x=400, y=170)
    
    identificador = tk.Entry(root)
    identificador.place(x=270, y=50)
    
    title = tk.Entry(root)
    title.place(x=270, y=80)
    
    writer = tk.Entry(root)
    writer.place(x=270, y=110)
    
    editorial = tk.Entry(root)
    editorial.place(x=270, y=140)
    
    publication = tk.Entry(root)
    publication.place(x=270, y=170)
    
    price = tk.Entry(root)
    price.place(x=270, y=200)
    
    entry_editorial = tk.Entry(root)
    entry_editorial.place(x=400, y=200)
    
    tk.Button(root,text="Crear",command=add, height=5, width=10, font=("Arial",12)).place(x=100,y=230)
    tk.Button(root,text="Editar",command=edit, height=5, width=10, font=("Arial",12)).place(x=250,y=230)
    tk.Button(root,text="Eliminar",command=delete, height=5, width=10, font=("Arial",12)).place(x=400,y=230)
    tk.Button(root,text="Filtrar",command=filtrar_por_editorial, height=5, width=10, font=("Arial",12)).place(x=550,y=230)
    
    columnas = ("Id","Titulo","Autor","Editorial","Publicación","Precio")
    listbox = ttk.Treeview(root,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=350)
    
    mostrar()
    listbox.bind("<Double-Button-1>", obtenerR)
    
    root.mainloop()

#! LOGIN

def verificar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='proyecto'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
        ''', (usuario, contraseña))
 
        usuario = cursor.fetchone()
 
        if usuario:
            
            if usuario[5] == "Administrador":
                messagebox.showinfo("Login exitoso", f"Bienvenido Administrador {usuario[1]}")
                root.withdraw()
                mostrar_gestion_empleados()
                
            elif usuario[5] == "Empleado":
                messagebox.showinfo("Login exitoso", f"Bienvenido Empleado {usuario[1]}")
                root.withdraw()
                mostrar_gestion_libros()
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  
 
root = tk.Tk()
root.title("Login")
root.geometry("300x200")
 
label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)
 
btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 
root.mainloop()