from PyQt5 import uic, QtWidgets

class Janelas():
    #Construtor
    def __init__(self, menu_principal=None):
        self.menu_principal = menu_principal

    #Métodos
    def menu_inicial(self):
        self.menu_principal = uic.loadUi("janelas/menu_inicial.ui")
        self.menu_principal.show()