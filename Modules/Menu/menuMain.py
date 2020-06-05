# coding=utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *
import sys

class Pantalla(QWidget):
    def __init__(self,changeToLoIn,changeToRegister,endApp):
        print('__init__() menuMain.py')
        super(QWidget, self).__init__()
        self.__changeToLogIn=changeToLoIn
        self.__changeToRegister=changeToRegister
        self.__endApp=endApp
        self.initUI()

    def initUI(self):
        print('initUI() menuMain.py')
        self.SetTittle()
        self.InputDialog()
        self.initWindowUILayout()

    def initWindowUILayout(self):
        print('initWindowUILayout() menuMain.py')
        self.mainLayout = QHBoxLayout()
        self.graphLayout = QVBoxLayout()
        self.contectivityLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        self.setLayout(self.mainLayout)

    def SetTittle(self):
        print('SetTitle()menuMain.py')
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
        print('InputDialog() menuMain.py')
        positionY = 450
        positionX = 830
        btnOk = QPushButton('Iniciar Sesión', self)
        btnOk.move(positionX, positionY)
        btnOk.resize(250, 75)
        btnOk.setFont(QFont('SansSerif', 18))
        #btnOk.clicked.connect(self.openArchivoMain)
        btnOk.clicked.connect(self.__changeToLogIn)
        #btnOk.clicked.connect(self.comprobarUsuarioContra())

        btnRegistro = QPushButton('Registrarse', self)
        btnRegistro.move(positionX, positionY + 100)
        btnRegistro.resize(250, 75)
        btnRegistro.setFont(QFont('SansSerif', 18))
        btnRegistro.clicked.connect(self.__changeToRegister)

        btnRegistro = QPushButton('Salir', self)
        btnRegistro.move(positionX, positionY + 200)
        btnRegistro.resize(250, 75)
        btnRegistro.setFont(QFont('SansSerif', 18))
        btnRegistro.clicked.connect(self.__endApp)

    def comprobarUsuarioContra(self, user, contra):
        print ('comprobarUsuarioContra() menuMain.py')
        if (len(user) < 8 or len(contra) < 8):
            self.showDialog("Estatus de registro", "Usuario/Contrasena muy corto", QMessageBox.Warning)
        else:
            self.showDialog("Estatus de registro", "El usuario \"" + user + "\" ha sido registrado correctamente",
                            QMessageBox.Information)
            file = open("../Usuarios.txt", "a")
            file.write(user + "\n" + contra + "\n")
            file.close()
        #mainRe.MainRe.main()

    def showDialog(self, titulo, textoCuerpo, icon):
        print('showDialog() menuMain.py')
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()