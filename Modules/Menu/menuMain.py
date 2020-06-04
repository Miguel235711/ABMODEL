# coding=utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *
import sys
sys.path.append("../Registration")
import mainRe

class Pantalla(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.SetTittle()
        self.InputDialog()
        self.initWindowUILayout()

    def initWindowUILayout(self):
        self.mainLayout = QHBoxLayout()
        self.graphLayout = QVBoxLayout()
        self.contectivityLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        self.setLayout(self.mainLayout)

    def SetTittle(self):
        l1 = QLabel(self)
        l1.setText("ABMODEL SYSTEM")
        l1.move(0, 0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920, 540)
        l1.setFont(QFont('SansSerif', 50))

        l2 = QLabel(self)
        l2.setText("Menu Principal")
        l2.move(0, 0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920, 670)
        l2.setFont(QFont('SansSerif', 25))

    def InputDialog(self):
        positionY = 450
        positionX = 830
        btnOk = QPushButton('Iniciar Sesión', self)
        btnOk.move(positionX, positionY)
        btnOk.resize(250, 75)
        btnOk.setFont(QFont('SansSerif', 18))
        btnOk.clicked.connect(self.openArchivoMain)
        #btnOk.clicked.connect(self.comprobarUsuarioContra())

        btnRegistro = QPushButton('Registrarse', self)
        btnRegistro.move(positionX, positionY + 100)
        btnRegistro.resize(250, 75)
        btnRegistro.setFont(QFont('SansSerif', 18))

    def comprobarUsuarioContra(self, user, contra):
        if (len(user) < 8 or len(contra) < 8):
            self.showDialog("Estatus de registro", "Usuario/Contrasena muy corto", QMessageBox.Warning)
        else:
            self.showDialog("Estatus de registro", "El usuario \"" + user + "\" ha sido registrado correctamente",
                            QMessageBox.Information)
            file = open("../Usuarios.txt", "a")
            file.write(user + "\n" + contra + "\n")
            file.close()

    def openArchivoMain(self):
        print "Hello World"
        mainRe.main()

    def showDialog(self, titulo, textoCuerpo, icon):
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()