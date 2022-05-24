from PyQt5 import uic, QtWidgets

import random

class Forca():
    #Construtor
    def __init__(self, palavras=[], dicas=[],letras_certas=[]):
        #--Instanciando variáveis
        self.dicas = dicas
        self.letras_certas = letras_certas
        self.palavras = palavras


    #Métodos
    def sorteio(self):
        #--Sorteia um número
        sorteio = random.randint(0, 3)
        #--Retorna o número
        return sorteio

    def palavra_secreta(self):
        #--Cria lista de palavras
        self.palavras = ['Pave'.upper(), 'Queijo'.upper(), 'Hamburguer'.upper()]
        #--Palavra sorteada de acordo com a sua posição
        palavra_sorteada = self.palavras[self.sorteio()]
        #--Retorna a palavra sorteada
        return palavra_sorteada

    def dica_secreta(self, tela):
        #--Cria lista de dicas
        self.dicas = ['Sobremesa', 'Vem do leite', 'Tem dentro do lanche']
        #--Dica sorteada de acordo com a sua posição
        dica_sorteada = self.dicas[self.sorteio()]
        #--Escreve a dica no label da tela
        tela.dica.setText(dica_sorteada)