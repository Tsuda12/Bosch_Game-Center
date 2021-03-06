# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forca.ui'
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
        Form.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/hangman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lbl_nome_2 = QtWidgets.QLabel(Form)
        self.lbl_nome_2.setGeometry(QtCore.QRect(10, 30, 681, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_2.setFont(font)
        self.lbl_nome_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lbl_nome_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(85, 255, 255);")
        self.lbl_nome_2.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_nome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nome_2.setObjectName("lbl_nome_2")
        self.lbl_dica = QtWidgets.QLabel(Form)
        self.lbl_dica.setGeometry(QtCore.QRect(10, 140, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dica.setFont(font)
        self.lbl_dica.setStyleSheet("color: rgb(255, 85, 127);")
        self.lbl_dica.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dica.setObjectName("lbl_dica")
        self.lbl_txt_dica = QtWidgets.QLabel(Form)
        self.lbl_txt_dica.setGeometry(QtCore.QRect(150, 180, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_txt_dica.setFont(font)
        self.lbl_txt_dica.setStyleSheet("border: 1px solid rgb(255, 85, 127);\n"
"color: white;")
        self.lbl_txt_dica.setText("")
        self.lbl_txt_dica.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_txt_dica.setObjectName("lbl_txt_dica")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 239, 211, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: white;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lne_chute = QtWidgets.QLineEdit(Form)
        self.lne_chute.setGeometry(QtCore.QRect(150, 590, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(11)
        font.setItalic(True)
        self.lne_chute.setFont(font)
        self.lne_chute.setStyleSheet("border: 1px solid rgb(0, 255, 255);\n"
"color: white;")
        self.lne_chute.setMaxLength(1)
        self.lne_chute.setAlignment(QtCore.Qt.AlignCenter)
        self.lne_chute.setObjectName("lne_chute")
        self.btn_enviar = QtWidgets.QPushButton(Form)
        self.btn_enviar.setGeometry(QtCore.QRect(460, 590, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enviar.setStyleSheet("border: 1px solid rgb(255, 85, 127);\n"
"color: white;\n"
"")
        self.btn_enviar.setObjectName("btn_enviar")
        self.lbl_palavra_secreta = QtWidgets.QLabel(Form)
        self.lbl_palavra_secreta.setGeometry(QtCore.QRect(150, 520, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_palavra_secreta.setFont(font)
        self.lbl_palavra_secreta.setStyleSheet("border: 1px solid rgb(255, 85, 127);\n"
"color: white;")
        self.lbl_palavra_secreta.setText("")
        self.lbl_palavra_secreta.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_palavra_secreta.setObjectName("lbl_palavra_secreta")
        self.lbl_letras_erradas = QtWidgets.QLabel(Form)
        self.lbl_letras_erradas.setGeometry(QtCore.QRect(380, 266, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_letras_erradas.setFont(font)
        self.lbl_letras_erradas.setStyleSheet("border: 1px solid rgb(255, 85, 127);\n"
"color: white;")
        self.lbl_letras_erradas.setText("")
        self.lbl_letras_erradas.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_letras_erradas.setObjectName("lbl_letras_erradas")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 240, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.ganhou = QtWidgets.QLabel(Form)
        self.ganhou.setGeometry(QtCore.QRect(390, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ganhou.setFont(font)
        self.ganhou.setStyleSheet("color: rgb(0, 255, 0);")
        self.ganhou.setAlignment(QtCore.Qt.AlignCenter)
        self.ganhou.setObjectName("ganhou")
        self.perdeu = QtWidgets.QLabel(Form)
        self.perdeu.setGeometry(QtCore.QRect(390, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.perdeu.setFont(font)
        self.perdeu.setStyleSheet("color: rED;")
        self.perdeu.setAlignment(QtCore.Qt.AlignCenter)
        self.perdeu.setObjectName("perdeu")
        self.btn_enviar_2 = QtWidgets.QPushButton(Form)
        self.btn_enviar_2.setGeometry(QtCore.QRect(580, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_enviar_2.setFont(font)
        self.btn_enviar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enviar_2.setStyleSheet("border: 1px solid rgb(255, 85, 127);\n"
"color: white;\n"
"")
        self.btn_enviar_2.setObjectName("btn_enviar_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Jogo da Forca"))
        self.lbl_nome_2.setText(_translate("Form", "<html><head/><body><p>JOGO DA FORCA</p></body></html>"))
        self.lbl_dica.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ff557f;\">DICA</span></p></body></html>"))
        self.label.setText(_translate("Form", "a"))
        self.lne_chute.setPlaceholderText(_translate("Form", "Insira uma letra"))
        self.btn_enviar.setText(_translate("Form", "CHUTAR"))
        self.label_2.setText(_translate("Form", "LETRAS ERRADAS"))
        self.ganhou.setText(_translate("Form", "VOC?? GANHOU!"))
        self.perdeu.setText(_translate("Form", "VOC?? PERDEU!"))
        self.btn_enviar_2.setText(_translate("Form", "REJOGAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
