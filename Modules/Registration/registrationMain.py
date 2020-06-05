from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *

import sys
sys.path.append("../Authentication")
import authenticationMain as auMain

class Pantalla(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        self.SetTittle()
        self.InputDialog()
        self.initWindowUILayout()

    def initWindowUILayout(self):
        self.mainLayout=QHBoxLayout()
        self.graphLayout=QVBoxLayout()
        self.contectivityLayout=QVBoxLayout()
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        self.setLayout(self.mainLayout)

    def SetTittle(self):
        l1 = QLabel(self)
        l1.setText("ABMODEL SYSTEM")
        l1.move(0,0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920,540)
        l1.setFont(QFont('SansSerif', 50))

        l2 = QLabel(self)
        l2.setText("Sistema de registro")
        l2.move(0,0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920,670)
        l2.setFont(QFont('SansSerif', 25))

    def InputDialog(self):
        usrInputText = QLabel(self)
        usrInputText.setText("Usuario :")
        usrInputText.move(-100,450)
        usrInputText.setAlignment(Qt.AlignCenter)
        usrInputText.resize(1920,35)
        usrInputText.setFont(QFont('SansSerif', 20))

        usrInput = QLineEdit(self)
        usrInput.setPlaceholderText("Ingresa tu usuario")
        usrInput.move(950,450)
        usrInput.setAlignment(Qt.AlignCenter)
        usrInput.resize(200,35)

        passInputText = QLabel(self)
        passInputText.setText("Contrasena :")
        passInputText.move(-100,550)
        passInputText.setAlignment(Qt.AlignCenter)
        passInputText.resize(1920,35)
        passInputText.setFont(QFont('SansSerif', 20))

        passInput = QLineEdit(self)
        passInput.setPlaceholderText("Ingresa tu contrasena")
        passInput.move(950,550)
        passInput.setEchoMode(QLineEdit.Password)
        passInput.setAlignment(Qt.AlignCenter)
        passInput.resize(200,35)

        btnOk = QPushButton('Aceptar',self)
        btnOk.move(850,650)
        btnOk.clicked.connect(lambda: self.comprobarUsuarioContra(usrInput.text(),passInput.text()))

        btn = QPushButton('Cancelar',self)
        btn.move(1000,650)

    def comprobarUsuarioContra(self,user,contra):
        if(len(user) < 8 or len(contra) < 8):
            self.showDialog("Estatus de registro", "Usuario/Contrasena muy corto",QMessageBox.Warning)
        else:
            self.showDialog("Estatus de registro", "El usuario \""+user+"\" ha sido registrado correctamente" ,QMessageBox.Information)
            file = open("../Usuarios.txt","a")

            file.write(auMain.main(str(user),str(contra))+"\n")
            file.close()
            
    
    def showDialog(self,titulo,textoCuerpo,icon):
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()