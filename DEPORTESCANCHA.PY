class DeportesCancha:
    def __init__(self,nombre,cj,reglamento):
        self.nombre=nombre
        self.cj=cj
        self.reglamento=reglamento
        
    def mostrar(self):
        print("Nombre deporte:",self.nombre,"\nCantidad de Jugadores: ",self.cj)
        print("Reglamento:")
        for c,v in self.reglamento.items():
            print(c," ",v)
class Futbol(DeportesCancha): 
    def __init__(self,nombre,cj,reglamento,tiemporeglamentario):
      super().__init__(nombre,cj,reglamento)
      self.tiemporeglamentario=tiemporeglamentario
      
        
    def mostrar(self):
      super().mostrar()
      print("TIEMPO REGLAMENTARIO: ",self.tiemporeglamentario) 
      
class Tenis(DeportesCancha):     
    def __init__(self,nombre,cj,reglamento,tiemporeglamentario):
      super().__init__(nombre,cj,reglamento)
      self.tiemporeglamentario=tiemporeglamentario
      
        
    def mostrar(self):
      super().mostrar()
      print("TIEMPO REGLAMENTARIO: ",self.tiemporeglamentario)   
reglamento={"1":"regla1","2":"regla2"}
f=Futbol("Futbol",10,reglamento,40)
f.mostrar()
t=Tenis("Tenis",2,reglamento,40)
t.mostrar()