# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jokenpo.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 700)
        Form.setMinimumSize(QtCore.QSize(700, 700))
        Form.setMaximumSize(QtCore.QSize(700, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/jokenpo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background: black\n"
"")
        self.lbl_nome = QtWidgets.QLabel(Form)
        self.lbl_nome.setGeometry(QtCore.QRect(10, 30, 681, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lbl_nome.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(85, 255, 255);")
        self.lbl_nome.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nome.setObjectName("lbl_nome")
        self.lbl_pedra = QtWidgets.QLabel(Form)
        self.lbl_pedra.setGeometry(QtCore.QRect(90, 160, 128, 128))
        self.lbl_pedra.setMinimumSize(QtCore.QSize(128, 128))
        self.lbl_pedra.setText("")
        self.lbl_pedra.setPixmap(QtGui.QPixmap("../img/pedra.png"))
        self.lbl_pedra.setScaledContents(True)
        self.lbl_pedra.setObjectName("lbl_pedra")
        self.lbl_papel = QtWidgets.QLabel(Form)
        self.lbl_papel.setGeometry(QtCore.QRect(292, 160, 128, 128))
        self.lbl_papel.setMinimumSize(QtCore.QSize(128, 128))
        self.lbl_papel.setText("")
        self.lbl_papel.setPixmap(QtGui.QPixmap("../img/folha-de-papel.png"))
        self.lbl_papel.setScaledContents(True)
        self.lbl_papel.setObjectName("lbl_papel")
        self.lbl_tesoura = QtWidgets.QLabel(Form)
        self.lbl_tesoura.setGeometry(QtCore.QRect(500, 160, 128, 128))
        self.lbl_tesoura.setMinimumSize(QtCore.QSize(128, 128))
        self.lbl_tesoura.setText("")
        self.lbl_tesoura.setPixmap(QtGui.QPixmap("../img/tesoura.png"))
        self.lbl_tesoura.setScaledContents(True)
        self.lbl_tesoura.setObjectName("lbl_tesoura")
        self.btn_pedra = QtWidgets.QPushButton(Form)
        self.btn_pedra.setGeometry(QtCore.QRect(103, 310, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pedra.setFont(font)
        self.btn_pedra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pedra.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"outiline:none;\n"
"border: none;")
        self.btn_pedra.setObjectName("btn_pedra")
        self.btn_papel = QtWidgets.QPushButton(Form)
        self.btn_papel.setGeometry(QtCore.QRect(306, 310, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_papel.setFont(font)
        self.btn_papel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_papel.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"outiline:none;\n"
"border: none;")
        self.btn_papel.setObjectName("btn_papel")
        self.btn_tesoura = QtWidgets.QPushButton(Form)
        self.btn_tesoura.setGeometry(QtCore.QRect(514, 310, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_tesoura.setFont(font)
        self.btn_tesoura.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_tesoura.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"outiline:none;\n"
"border: none;")
        self.btn_tesoura.setObjectName("btn_tesoura")
        self.lbl_sorteio = QtWidgets.QLabel(Form)
        self.lbl_sorteio.setGeometry(QtCore.QRect(180, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sorteio.setFont(font)
        self.lbl_sorteio.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_sorteio.setObjectName("lbl_sorteio")
        self.lbl_sorteio_computador = QtWidgets.QLabel(Form)
        self.lbl_sorteio_computador.setGeometry(QtCore.QRect(350, 488, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sorteio_computador.setFont(font)
        self.lbl_sorteio_computador.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 127);")
        self.lbl_sorteio_computador.setObjectName("lbl_sorteio_computador")
        self.lbl_sorteio_2 = QtWidgets.QLabel(Form)
        self.lbl_sorteio_2.setGeometry(QtCore.QRect(230, 590, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_sorteio_2.setFont(font)
        self.lbl_sorteio_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_sorteio_2.setObjectName("lbl_sorteio_2")
        self.lbl_selecionado = QtWidgets.QLabel(Form)
        self.lbl_selecionado.setGeometry(QtCore.QRect(230, 410, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_selecionado.setFont(font)
        self.lbl_selecionado.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_selecionado.setObjectName("lbl_selecionado")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Jogo Jokenpo"))
        self.lbl_nome.setText(_translate("Form", "<html><head/><body><p>JOGO JOKENPO</p></body></html>"))
        self.btn_pedra.setText(_translate("Form", "PEDRA"))
        self.btn_papel.setText(_translate("Form", "PAPEL"))
        self.btn_tesoura.setText(_translate("Form", "TESOURA"))
        self.lbl_sorteio.setText(_translate("Form", "<html><head/><body><p>COMPUTADOR:</p></body></html>"))
        self.lbl_sorteio_computador.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lbl_sorteio_2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lbl_selecionado.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
