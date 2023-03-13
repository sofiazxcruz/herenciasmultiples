class Categorias:
    pass
    categoria1="Accion"
    categoria2="Terror"
    categoria3="Comedia"
    
    from Categorias import Categorias

class Peliculas(Categorias):
    pass
    
    def __init__(self,Pelicula1,Pelicula2,pelicula3):
        
        self.Pelicula1=Pelicula1
        self.Pelicula2=Pelicula2
        self.Pelicula3=pelicula3
        

    def CategoriaAccion(self):
        return"\n Las siguientes peliculas son de la categoria: {}  son \n {} \n {}  \n {}".format(Categorias.categoria1,self.Pelicula1,self.Pelicula2,self.Pelicula3)
    
    def CategoriaTerror(self):
        return"\n Las siguientes peliculas son de la categoria: {}  son \n {} \n {}  \n {}".format(Categorias.categoria2,self.Pelicula1,self.Pelicula2,self.Pelicula3)

    def CategoriaComedia(self):
        return"\n Las siguientes peliculas son de la categoria: {}  son \n {} \n {}  \n {}".format(Categorias.categoria3,self.Pelicula1,self.Pelicula2,self.Pelicula3)

    
verCategoria1 = Peliculas("Black Panther","Logan","RRR")
print(verCategoria1.CategoriaAccion())
verCategoria2 = Peliculas("Human Centepide","Scream","Smile")
print(verCategoria2.CategoriaTerror())
verCategoria3 = Peliculas("TED","Minions","Borat")
print(verCategoria3.CategoriaComedia())

from Peliculas import Peliculas
from Peliculas import verCategoria3

class Cliente (Peliculas):
      
    def __init__(self, Pelicula1):
        
        self.Pelicula1=Pelicula1
        
 
    def ValidarPeli(self):
        Validacion1=verCategoria3.Pelicula1

        if Validacion1 ==self.Pelicula1:
            print("\n ////////////////////////////////////////////////////////////////////////////////////////////////")
            print("\n                        Eligio la categoria de comedia. Su pelicula es TED"                       )
            print("\n ////////////////////////////////////////////////////////////////////////////////////////////////")
        else:
            print("Error")

Progra1 = Cliente("TED")
print(Progra1.ValidarPeli())