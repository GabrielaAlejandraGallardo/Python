"""En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos,
 imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."""
class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def mostrar(self):
        if self.nota >=7:
           print("El estudiante: ", self.nota, " con nota: ", self.nota, "ha aprobado")    
        else:
           print("El estudiante: ", self.nota, " con nota: ", self.nota, "no ha aprobado")     

nombre=input("Introduce nombre del estudiante: ")
nota=float(input("Introduce su nota: "))
a1=Alumno(nombre, nota)
a1.mostrar()
nombre=input("Introduce nombre del estudiante: ")
nota=float(input("Introduce su nota: "))
a2=Alumno(nombre, nota)
a2.mostrar()