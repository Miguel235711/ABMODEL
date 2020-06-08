# encoding: utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout,QGridLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *
import sys
sys.path.append("../Authentication")
import authenticationMain as auMain
sys.path.append("../CommonWidgets")
import dummy
import styles
sys.path.append('../GlobalInstances')
import globalInstances

class Pantalla(QWidget):
    def __init__(self,changeToMainMenu):
        super(QWidget,self).__init__()
        self.__changeToMainMenu=changeToMainMenu
        self.__dialog=globalInstances.GlobalInstances.getInstance('infoDialog')
        self.initUI()
    def initUI(self):
        self.__mainLayout=QVBoxLayout()
        self.setLayout(self.__mainLayout)
        self.SetTittle()
        self.InputDialog()

    def SetTittle(self):
        l1 = QLabel()
        l1.setText("ABMODEL SYSTEM")
        #l1.move(0,0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920,540)
        l1.setFont(QFont('SansSerif', 50))
        self.__mainLayout.addWidget(l1)
        
        l2 = QLabel()
        l2.setText("Sistema de registro")
        l2.move(0,0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920,670)
        l2.setFont(QFont('SansSerif', 25))
        self.__mainLayout.addWidget(l2)

    def InputDialog(self):
        
        inputGridLayout=QGridLayout()
        
        usrInputText = QLabel()
        usrInputText.setText("Usuario :")
        #usrInputText.move(-100,450)
        usrInputText.setAlignment(Qt.AlignCenter)
        usrInputText.resize(1920,35)
        usrInputText.setFont(QFont('SansSerif', 20))
        inputGridLayout.addWidget(dummy.getDummyWidget(),0,0)
        inputGridLayout.addWidget(usrInputText,0,1)
        
        usrInput = QLineEdit()
        usrInput.setPlaceholderText("Ingresa tu usuario")
        #usrInput.move(950,450)
        usrInput.setAlignment(Qt.AlignCenter)
        usrInput.setFixedHeight(35)
        inputGridLayout.addWidget(usrInput,0,2)
        inputGridLayout.addWidget(dummy.getDummyWidget(),0,3)

        self.__mainLayout.addLayout(inputGridLayout)
        

        passInputText = QLabel()
        passInputText.setText(u'Contraseña :')
        #passInputText.move(-100,550)
        passInputText.setAlignment(Qt.AlignCenter)
        passInputText.resize(1920,35)
        passInputText.setFont(QFont('SansSerif', 20))
        inputGridLayout.addWidget(dummy.getDummyWidget(),1,0)
        inputGridLayout.addWidget(passInputText,1,1)

        passInput = QLineEdit()
        passInput.setPlaceholderText(u'Ingresa tu contraseña')
        #passInput.move(950,550)
        passInput.setEchoMode(QLineEdit.Password)
        passInput.setAlignment(Qt.AlignCenter)
        passInput.setFixedHeight(35)
        inputGridLayout.addWidget(passInput,1,2)
        inputGridLayout.addWidget(dummy.getDummyWidget(),1,3)

        btonOkLayout=QHBoxLayout()

        btnOk = QPushButton('Aceptar')
        btonOkLayout.addWidget(dummy.getDummyWidget())
        btonOkLayout.addWidget(btnOk)
        btonOkLayout.addWidget(dummy.getDummyWidget())
        #btnOk.move(850,650)
        btnOk.clicked.connect(lambda: self.comprobarUsuarioContra(usrInput.text(),passInput.text()))

        self.__mainLayout.addLayout(btonOkLayout)

        btnLayout=QHBoxLayout()

        btn = QPushButton('Cancelar')
        btnLayout.addWidget(dummy.getDummyWidget())
        btnLayout.addWidget(btn)
        btnLayout.addWidget(dummy.getDummyWidget())
        btn.clicked.connect(self.__changeToMainMenu)

        self.__mainLayout.addLayout(btnLayout)

        self.setStyleSheet(styles.buttonStyleSheet)

        #btn.move(1000,650)

    def comprobarUsuarioContra(self,user,contra):
        if(len(user) < 8 or len(contra) < 8):
            self.__dialog.openWarningDialog("Estatus de registro", 'Usuario/Contraseña muy corto')
        else:
            file = open("../Usuarios.txt","a")
            print 'user:',user,'password:',contra
            #file.write(auMain.main(str(user),str(contra))+"\n")
            file.write(str(user)+":"+str(contra)+"\n")
            file.close()
            self.__dialog.openSuccessDialog("Estatus de registro", "El usuario \""+user+"\" ha sido registrado correctamente")
            self.__changeToMainMenu()