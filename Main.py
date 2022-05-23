from PyQt5 import uic, QtWidgets
from Menu import Menu

if __name__ == '__main__':
    #Instâncias
    app = QtWidgets.QApplication([])
    menu = Menu()

    #Ações
    #--Chama o método da janela
    menu.iniciar()
    #--Executa o app
    app.exec()