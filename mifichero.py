import pickle
class Juguete:   
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre
#j1=Juguete("Dino",18.4)
#f=open("datos.bin","wb")
#pickle.dump(j1,f)
f=open("datos.bin","rb")
Dino=pickle.load(f)
f.close()
print(type(Dino))
print(Dino.getNombre(),"precio",Dino.precio)

class Estado:
    players=Players()
    status=Status()
    life_remaining=12
    armor=False
f=open("gamestatus.dat","wb")
e=Estado()   
pickle.dumps(f,e)
f.close() 