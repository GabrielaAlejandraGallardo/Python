from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
root=Tk()
root.title("aplicacion crud con base de datos")
root.geometry("600x350")
miId=StringVar()
miNombre=StringVar()
miCargo=StringVar()
miSalario=StringVar()
def conexionBBDD():
   miConexion=sqlite3.connect("base")
   miCursor=miConexion.cursor()
   try:
       miCursor.execute('''
       CREATE TABLE empleado (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50) NOT NULL,
        CARGO VARCHAR(50) NOT NULL,
        SALARIO INT NOT NULL)''')
       
       messagebox.showinfo("CONEXION","BASE DE DATOS CREADA EXITOSAMENTE")
   except:     
         messagebox.showinfo("CONEXION","CONECXION EXITOSA CON BASE DE DATOS")
def eliminarBBDD():
    miConexion=sqlite3.connect("base")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="los datos se perderan para siempre ¿Desea continuar:"):
       miCursor.execute("DROP TABLE empleado")
    else:
        pass
def salirAplicación():
    valor=messagebox.askquestion("salir","¿Estas seguro que deseas salir de la aplicaion")     
    if valor=="yes":
        root.destroy()
def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")      
    miSalario.set("")
def mensaje():
    acerca='''Aplicación Crud version 0.1 tencología python Tkinter'''
    messagebox.showinfo(title="INFORMACIÓN",Message=acerca)
    ###metodos
def crear():
    miConexion = sqlite3.connect("base")
    miCursor = miConexion.cursor()
  ##  miConexion=sqlite3.connect("base")
    ##miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("INSERT INTO empleado VALUES(NULL,?,?,?)",(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Ocurrio un error al crear VERIFIQUE CONEXION CON BASE DE DATOS")
        
    limpiarCampos()
    mostrar()
def mostrar():
    miConexion=sqlite3.connect("base")            
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM empleado")   
        for row in miCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
    except:
        pass
####tabla
tree=ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0,y=130)
tree.column('#0',width=100)
tree.heading('#0', text="id",anchor=CENTER)
tree.heading('#1', text="Nombre del Empleado",anchor=CENTER)
tree.heading('#2', text="Cargo",anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text="Salario",anchor=CENTER)

def seleccionarUsandoClick(event):
    item=tree.identify('item',event.x,event.y)
    miId.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miCargo.set(tree.item(item,"values")[1])
    miSalario.set(tree.item(item,"values")[2])
tree.bind("<Double-1>",seleccionarUsandoClick)    

def actualizar():
    miConexion=sqlite3.connect("base")            
    miCursor=miConexion.cursor()
    try:
        datos=miNombre.get(),miCargo.get(),miSalario.get()
        miCursor.execute("UPDATE empleado SET NOMBRE=?,CARGO=?,SALARIO=? WHERE ID="+miId.get(),(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","Se actualizaron los datos")
        pass
    limpiarCampos()
    mostrar()
def borrar():
     miConexion=sqlite3.connect("base")            
     miCursor=miConexion.cursor()
     try:
         if messagebox.askyesno(message="realmente quieres eliminar el registro¿", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM empleado WHERE ID="+miId.get())
            miConexion.commit()
     except:
            messagebox.showwarning("Advertencia","OURRIO UN ERROR A LA HORA DE TRATAR DE ELIMINAR EL REGISTRO")
     limpiarCampos()
     mostrar()

#colocamos widgets en la vista
#creamos menu
menubar=Menu(root)        
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/conectar base de dartos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicación)
menubar.add_cascade(label="inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)
#creamos etiquetas y cajas de texto
e1=Entry(root,textvariable=miId)

l2=Label(root,text="Nombre")
l2.place(x=50,y=10)
e2=Entry(root,textvariable=miNombre, width=50)
e2.place(x=100,y=10)

l3=Label(root,text="Cargo")
l3.place(x=50,y=40)
e3=Entry(root,textvariable=miCargo)
e3.place(x=100,y=40)

l4=Label(root,text="Salario")
l4.place(x=280,y=40)
e4=Entry(root,textvariable=miSalario, width=10)
e4.place(x=320,y=40)

l5=Label(root,text="UDS")
l5.place(x=380,y=40)

######creamos botones
b1=Button(root, text="Crear registro", command=crear)
b1.place(x=50,y=90)
b2=Button(root, text="Modificar registro", command=actualizar)
b2.place(x=180,y=90)
b3=Button(root, text="Mostrar registro", command=mostrar)
b3.place(x=320,y=90)
b4=Button(root, text="Eliminar registro" ,command=borrar)
b4.place(x=450,y=90)

root.config(menu=menubar)
root.mainloop()