from tkinter import *  
from PIL import ImageTk,Image  

ws = Tk()  
ws.title('PythonGuides')
ws.geometry('500x500')

canvas = Canvas(
        ws, 
        width = 500, 
        height = 500
        )  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open('imagen.gif'))  
canvas.create_image(
        10, 
        10, 
        anchor=NW, 
        image=img
        ) 
button=Button(ws,image=img).pack(padx=10,pady=30)

ws.mainloop() 