from Menu import Menu
import random

class Forca(Menu):
    #Construtor
    def __init__(self, dicas=[],letras_certas=[]):
        #--Super da classe Menu
        super(Forca, self).__init__(menu_principal, jogo_forca)
        #--Instanciando variáveis
        self.dicas = dicas
        self.letras_certas = letras_certas


    #Métodos
    def sorteio(self):
        #--Sorteia um número e retorna ele
        sorteio = random.randint(0, 3)
        return sorteio
