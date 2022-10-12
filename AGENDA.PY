from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
#from PIL import Image
root=Tk()
root.config(bg="lightgreen")
root.title("aplicacion crud con base de datos")
root.geometry("600x350")
ID=StringVar()
Dia=StringVar()
Horario=StringVar()
Actividad=StringVar()
Costo=StringVar()

def conexionBBDD():
   miConexion=sqlite3.connect("AGENDA.sqbpro")
   miCursor=miConexion.cursor()
   try:
       miCursor.execute('''
       CREATE TABLE "organizador" (
	"id"	INTEGER NOT NULL UNIQUE,
	"DIA"	INTEGER NOT NULL,
	"HORA"	INTEGER NOT NULL,
	"ACTIVIDAD"	TEXT NOT NULL,
	"COSTO"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);''')
    
       
       messagebox.showinfo("CONEXION","BASE DE DATOS CREADA EXITOSAMENTE")
   except:     
         messagebox.showinfo("CONEXION","CONECXION EXITOSA CON BASE DE DATOS")
def eliminarBBDD():
    miConexion=sqlite3.connect("AGENDA.sqbpro")
    miCursor=miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan para siempre ¿Desea continuar:"):
       miCursor.execute("DROP TABLE organizador")
    else:
        pass
def salirAplicación():
    valor=messagebox.askquestion("Salir","¿Estas seguro que deseas salir de la aplicación?")     
    if valor=="yes":
        root.destroy()
def limpiarCampos():
    ID.set("")
    Dia.set("")
    Horario.set("")      
    Actividad.set("")
    Costo.set("")

def mensaje():
    acerca="Aplicación de agenda"
    messagebox.showinfo("INFORMACIÓN",acerca)
    ###metodos
def crear():
    miConexion = sqlite3.connect("AGENDA.sqbpro")
    miCursor = miConexion.cursor()
    ##miCursor=miConexion.cursor()
    try:
        datos=Dia.get(),Horario.get(),Actividad.get(),Costo.get()
        miCursor.execute("INSERT INTO organizador VALUES(null,?,?,?,?)",(datos))
        miConexion.commit()
        
    except:
        messagebox.showwarning("Advertencia","--------Ocurrió un error al crear VERIFIQUE CONEXION CON BASE DE DATOS")
        
    limpiarCampos()
    mostrar()
def mostrar():
    miConexion=sqlite3.connect("AGENDA.sqbpro")            
    miCursor=miConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        miCursor.execute("SELECT * FROM organizador")   
        for row in miCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        messagebox.showinfo("Algo salió mal")
        
####tabla
tree=ttk.Treeview(height=10, columns=('#0','#1','#2',"#3","#4"))
tree.place(x=0,y=130)
tree.column('#0',width=30)
tree.heading('#1', text="Día",anchor=CENTER)
tree.heading('#0', text="ID",anchor=CENTER)
tree.heading('#2', text="Horario",anchor=CENTER)
tree.heading('#3', text="Actividad",anchor=CENTER)
tree.heading('#4', text="Costo",anchor=CENTER)

def seleccionarUsandoClick(event):
    item=tree.identify('item',event.x,event.y)
    ID.set(tree.item(item,"text"))
    Dia.set(tree.item(item,"values")[0])
    Horario.set(tree.item(item,"values")[1])
    Actividad.set(tree.item(item,"values")[2])
    Costo.set(tree.item(item,"values")[3])
tree.bind("<Double-1>",seleccionarUsandoClick)    

def actualizar():
    miConexion=sqlite3.connect("AGENDA.sqbpro")            
    miCursor=miConexion.cursor()
    try:
        datos=Dia.get(),Horario.get(),Actividad.get(),Costo.get()
        miCursor.execute("UPDATE organizador SET DIA=?,HORARIO=?,ACTIVIDAD=?,COSTO=? WHERE id="+ID.get(),(datos))
        miConexion.commit()
    except:
        messagebox.showwarning("Advertencia","No se puedieron actualizar los datos")
        
    limpiarCampos()
    mostrar()
def borrar():
     miConexion=sqlite3.connect("AGENDA.sqbpro")            
     miCursor=miConexion.cursor()
     try:
         if messagebox.askyesno(message="Desea eliminar el registro?", title="ADVERTENCIA"):
            miCursor.execute("DELETE FROM organizador WHERE id="+ID.get())
            miConexion.commit()
     except:
            messagebox.showwarning("Advertencia","OCURRIÓ UN ERROR A LA HORA DE TRATAR DE ELIMINAR EL REGISTRO")
     limpiarCampos()
     mostrar()

#colocamos widgets en la vista
#creamos menu
menubar=Menu(root)        
menubasedat=Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/conectar base de dartos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicación)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu=Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)
#creamos etiquetas y cajas de texto
l1=Label(root,text="ID")
l1.place(x=50,y=10)
e1=Entry(root,textvariable=ID, width=20)
e1.place(x=80, y=10)

l2=Label(root,text="Dia")
l2.place(x=250,y=10)
e2=Entry(root,textvariable=Dia, width=40)
e2.place(x=320,y=10)

l3=Label(root,text="Horario")
l3.place(x=50,y=40)
e3=Entry(root,textvariable=Horario, width=10)
e3.place(x=120,y=40)

l4=Label(root,text="Actividad")
l4.place(x=200,y=40)
e4=Entry(root,textvariable=Actividad, width=10)
e4.place(x=260,y=40)

l5=Label(root,text="Costo")
l5.place(x=400,y=40)
e5=Entry(root,textvariable=Costo, width=10)
e5.place(x=450,y=40)



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