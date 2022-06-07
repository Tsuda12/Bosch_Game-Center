# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'velha.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
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
        icon.addPixmap(QtGui.QPixmap("../img/tic-tac-toe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
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
        self.line = QtWidgets.QFrame(Form)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(110, 260, 500, 5))
        self.line.setMinimumSize(QtCore.QSize(500, 0))
        self.line.setMaximumSize(QtCore.QSize(500, 5))
        self.line.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setEnabled(True)
        self.line_2.setGeometry(QtCore.QRect(110, 410, 500, 5))
        self.line_2.setMinimumSize(QtCore.QSize(500, 0))
        self.line_2.setMaximumSize(QtCore.QSize(500, 5))
        self.line_2.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(270, 150, 5, 400))
        self.line_3.setMinimumSize(QtCore.QSize(5, 400))
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.line_3.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.line_3.setLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(440, 150, 5, 400))
        self.line_4.setMinimumSize(QtCore.QSize(5, 400))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 400))
        self.line_4.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(140, 150, 100, 100))
        self.btn_1.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_1.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_1.setText("")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(140, 290, 100, 100))
        self.btn_2.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_2.setText("")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(140, 430, 100, 100))
        self.btn_3.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_3.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(302, 150, 100, 100))
        self.btn_4.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_4.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(304, 290, 100, 100))
        self.btn_5.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(304, 430, 100, 100))
        self.btn_6.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(480, 150, 100, 100))
        self.btn_7.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_7.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(480, 290, 100, 100))
        self.btn_8.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_8.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(480, 430, 100, 100))
        self.btn_9.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_9.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: rgb(85, 255, 255);")
        self.btn_9.setText("")
        self.btn_9.setObjectName("btn_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 610, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lbl_venceu = QtWidgets.QLabel(Form)
        self.lbl_venceu.setGeometry(QtCore.QRect(490, 610, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_venceu.setFont(font)
        self.lbl_venceu.setStyleSheet("color: rgb(0, 255, 0)\n"
"")
        self.lbl_venceu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_venceu.setObjectName("lbl_venceu")
        self.lbl_venceu_2 = QtWidgets.QLabel(Form)
        self.lbl_venceu_2.setGeometry(QtCore.QRect(490, 610, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_venceu_2.setFont(font)
        self.lbl_venceu_2.setStyleSheet("color: rgb(0, 255, 0)\n"
"")
        self.lbl_venceu_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_venceu_2.setObjectName("lbl_venceu_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Jogo da Velha"))
        self.lbl_nome.setText(_translate("Form", "<html><head/><body><p>JOGO DA VELHA</p></body></html>"))
        self.label.setText(_translate("Form", "A"))
        self.lbl_venceu.setText(_translate("Form", "X VENCEU!"))
        self.lbl_venceu_2.setText(_translate("Form", "O VENCEU!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
