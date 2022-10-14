class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludo(self):
        print('hola, mi nombre es', self.nombre,'soy un', self.tipo, 'y mi sonido es el', self.sonido)


class Gato(Animal):
        tipo = 'felino'
        sonido = 'maullido'
        def __init__(self, nombre): #forma 1 de extender el __init__
            Animal.__init__(self, nombre)
            print('se ah registrado un gato')
        
class Perro(Animal):
        tipo = 'perruno'
        sonido = 'ladrido'
        def __init__(self, nombre):#forma 2 de extender el __init__
            super().__init__(nombre)
            print('se ah registrado un perro')
        
class Pajaro(Animal):
        tipo = 'ave'
        sonido = 'carareo'


gato = Gato('duquesa')
perro = Perro('flofy')

gato.saludo()
perro.saludo()
        

        
        