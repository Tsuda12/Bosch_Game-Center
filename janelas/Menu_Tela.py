# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(700, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowTitle("Central de Jogos")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: black;\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.menu_inicial = QtWidgets.QWidget(MainWindow)
        self.menu_inicial.setObjectName("menu_inicial")
        self.lbl_nome = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_nome.setGeometry(QtCore.QRect(10, 90, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setStyleSheet("color: rgb(255, 85, 127);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.lbl_nome.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nome.setObjectName("lbl_nome")
        self.lbl_nome_2 = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_nome_2.setGeometry(QtCore.QRect(15, 20, 681, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_2.setFont(font)
        self.lbl_nome_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 255);")
        self.lbl_nome_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_nome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nome_2.setObjectName("lbl_nome_2")
        self.img_forca = QtWidgets.QLabel(self.menu_inicial)
        self.img_forca.setGeometry(QtCore.QRect(182, 210, 131, 151))
        self.img_forca.setText("")
        self.img_forca.setPixmap(QtGui.QPixmap("../img/hangman.png"))
        self.img_forca.setScaledContents(False)
        self.img_forca.setObjectName("img_forca")
        self.lbl_titulo_forca = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_titulo_forca.setGeometry(QtCore.QRect(342, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_forca.setFont(font)
        self.lbl_titulo_forca.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);")
        self.lbl_titulo_forca.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo_forca.setObjectName("lbl_titulo_forca")
        self.lbl_descricao_forca = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_descricao_forca.setGeometry(QtCore.QRect(342, 259, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lbl_descricao_forca.setFont(font)
        self.lbl_descricao_forca.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_descricao_forca.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_descricao_forca.setObjectName("lbl_descricao_forca")
        self.btn_forca = QtWidgets.QPushButton(self.menu_inicial)
        self.btn_forca.setGeometry(QtCore.QRect(340, 320, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_forca.setFont(font)
        self.btn_forca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_forca.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"color: black;")
        self.btn_forca.setObjectName("btn_forca")
        self.lbl_descricao_velha = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_descricao_velha.setGeometry(QtCore.QRect(340, 489, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lbl_descricao_velha.setFont(font)
        self.lbl_descricao_velha.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_descricao_velha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_descricao_velha.setObjectName("lbl_descricao_velha")
        self.btn_velha = QtWidgets.QPushButton(self.menu_inicial)
        self.btn_velha.setGeometry(QtCore.QRect(338, 550, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_velha.setFont(font)
        self.btn_velha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_velha.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"color: black;")
        self.btn_velha.setObjectName("btn_velha")
        self.lbl_titulo_velha = QtWidgets.QLabel(self.menu_inicial)
        self.lbl_titulo_velha.setGeometry(QtCore.QRect(340, 450, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_velha.setFont(font)
        self.lbl_titulo_velha.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);")
        self.lbl_titulo_velha.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo_velha.setObjectName("lbl_titulo_velha")
        self.img_velha = QtWidgets.QLabel(self.menu_inicial)
        self.img_velha.setGeometry(QtCore.QRect(180, 440, 131, 151))
        self.img_velha.setText("")
        self.img_velha.setPixmap(QtGui.QPixmap("../img/tic-tac-toe.png"))
        self.img_velha.setScaledContents(False)
        self.img_velha.setObjectName("img_velha")
        MainWindow.setCentralWidget(self.menu_inicial)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_nome.setText(_translate("MainWindow", "<html><head/><body><p>FELIPE TSUDA</p></body></html>"))
        self.lbl_nome_2.setText(_translate("MainWindow", "<html><head/><body><p>CENTRAL JOGOS</p></body></html>"))
        self.lbl_titulo_forca.setText(_translate("MainWindow", "<html><head/><body><p>JOGO DA FORCA</p></body></html>"))
        self.lbl_descricao_forca.setText(_translate("MainWindow", "<html><head/><body><p>Acerte a palavra secreta<br/>para vencer o jogo.</p></body></html>"))
        self.btn_forca.setText(_translate("MainWindow", "JOGAR"))
        self.lbl_descricao_velha.setText(_translate("MainWindow", "<html><head/><body><p>Acerte uma sequência de 3<br/>e ganhe o jogo.</p></body></html>"))
        self.btn_velha.setText(_translate("MainWindow", "JOGAR"))
        self.lbl_titulo_velha.setText(_translate("MainWindow", "<html><head/><body><p>JOGO DA VELHA</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
