# coding=utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QToolTip, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *
import sys
sys.path.append("../CommonWidgets")
import styles

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
        self.__mainLayout=QVBoxLayout()
        self.setLayout(self.__mainLayout)
        self.SetTittle()
        self.InputDialog()

    def SetTittle(self):
        print('SetTitle()menuMain.py')
        l1 = QLabel()
        l1.setText("ABMODEL SYSTEM")
        #l1.move(0, 0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920, 540)
        l1.setFont(QFont('SansSerif', 50))

        self.__mainLayout.addWidget(l1,Qt.AlignHCenter)        

        l2 = QLabel()
        l2.setText(u'Menú Principal')
        #l2.move(0, 0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920, 670)
        l2.setFont(QFont('SansSerif', 25))

        self.__mainLayout.addWidget(l2,Qt.AlignHCenter)

    def InputDialog(self):
        print('InputDialog() menuMain.py')
        #positionY = 450
        #positionX = 830
        btnOk = QPushButton(u'Iniciar Sesión')
        #btnOk.move(positionX, positionY)
        #btnOk.resize(250, 75)
        btnOk.setFont(QFont('SansSerif', 18))
        #btnOk.clicked.connect(self.openArchivoMain)
        btnOk.clicked.connect(self.__changeToLogIn)

        self.__mainLayout.addWidget(btnOk,Qt.AlignHCenter)
        #btnOk.clicked.connect(self.comprobarUsuarioContra())

        btnRegistro = QPushButton('Registrarse')
       # btnRegistro.move(positionX, positionY + 100)
        #btnRegistro.setFixedSize(250, 75)
        btnRegistro.setFont(QFont('SansSerif', 18))
        btnRegistro.clicked.connect(self.__changeToRegister)
        self.__mainLayout.addWidget(btnRegistro,Qt.AlignHCenter)

        btnSalir = QPushButton('Salir')
        #btnRegistro.move(positionX, positionY + 200)
        #btnSalir.resize(250, 75)
        btnSalir.setFont(QFont('SansSerif', 18))
        btnSalir.clicked.connect(self.__endApp)
        self.__mainLayout.addWidget(btnSalir,Qt.AlignHCenter)
        self.__mainLayout.setAlignment(Qt.AlignHCenter)
        self.setStyleSheet(styles.buttonStyleSheet)