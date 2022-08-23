import pickle
class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
    def mostrar(self):   
        print("cant. de ruedas: ",self.ruedas," color: ",self.color, " puertas: ",self.puertas)
class Coche (Vehiculo):
     def __init__(self,velocidad,cilindrada):
        super().__init__()
        self.velocidad=velocidad
        self.cilindrada=cilindrada
     def mostrar(self):   
        super().mostrar()
        print(" velocidad: ",self.velocidad, "Cilindrada: ",self.cilindrada)
    
c=Vehiculo("azul",4,5)        
c.mostrar()

c1=Vehiculo("rojo",5,4)
f=open("fichero.bin","wb")
pickle.dump(c1,f)
f=open("fichero.bin","rb")
Dino=pickle.load(f)
#c=Vehiculo()   

f.close() 