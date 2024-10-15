class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def mover(self):
        print(self.nome, 'está se movendo')

class Voador:
    def voar(self):
        print('Estou voando')

class Aquatico:
    def nadar(self):
        print('Estou nadando')

class Pato(Animal, Voador, Aquatico):
    def __init__ (self, nome):
        super().__init__(nome)
        
pato = Pato("Donald")
print('-'*25)
pato.mover()
pato.nadar()
pato.voar()
print('-'*25)