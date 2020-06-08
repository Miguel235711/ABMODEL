from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QSizePolicy,QGridLayout,QMessageBox,QToolTip,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *

import sys
sys.path.append('../CommonWidgets')
import dummy
import styles
sys.path.append('../GlobalInstances')
import globalInstances

class Pantalla(QWidget):
    def __init__(self,changeToMainMenu,changeToUserMenu):
        print ('__init__() LogInMain')
        super(QWidget,self).__init__()
        self.__changeToUserMenu=changeToUserMenu
        self.__changeToMainMenu=changeToMainMenu
        self.__dialog=globalInstances.GlobalInstances.getInstance('infoDialog')
        self.initUI()

    def initUI(self):
        print ('initUI() LogInMain')
        self.__mainLayout=QVBoxLayout()
        self.setLayout(self.__mainLayout)
        self.SetTittle()
        self.InputDialog()
        #self.initWindowUILayout()
    def SetTittle(self):
        print ('SetTitle() LogInMain')
        l1 = QLabel()
        l1.setText("ABMODEL SYSTEM")
        #l1.move(0,0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920,540)
        l1.setFont(QFont('SansSerif', 50))

        self.__mainLayout.addWidget(l1,Qt.AlignHCenter)

        l2 = QLabel()
        l2.setText("Iniciar Sesion")
        #l2.move(0,0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920,670)
        l2.setFont(QFont('SansSerif', 25))

        self.__mainLayout.addWidget(l2,Qt.AlignHCenter)
    def InputDialog(self):
        print ('InputDialog() LogInMain')
        inputTextBoxesGrid=QGridLayout()

        usrInputText = QLabel()
        usrInputText.setText("Usuario :")
        #usrInputText.move(-100,450)
        usrInputText.setAlignment(Qt.AlignCenter)
        usrInputText.resize(1920,35)
        usrInputText.setFont(QFont('SansSerif', 20))

        inputTextBoxesGrid.addWidget(usrInputText,0,1)

        usrInput = QLineEdit()
        usrInput.setPlaceholderText("Ingresa tu usuario")
        #usrInput.move(950,450)
        usrInput.setAlignment(Qt.AlignCenter)
        usrInput.setFixedSize(450,35)

        inputTextBoxesGrid.addWidget(usrInput,0,2)

        inputTextBoxesGrid.addWidget(dummy.getDummyWidget(),0,3)
        inputTextBoxesGrid.addWidget(dummy.getDummyWidget(),0,0)
        inputTextBoxesGrid.setAlignment(Qt.AlignHCenter)
        passInputText = QLabel()
        passInputText.setText("Contrasena :")
        #passInputText.move(-100,550)
        passInputText.setAlignment(Qt.AlignCenter)
        passInputText.resize(1920,35)
        passInputText.setFont(QFont('SansSerif', 20))

        inputTextBoxesGrid.addWidget(passInputText,1,1)

        passInput = QLineEdit()
        passInput.setPlaceholderText("Ingresa tu contrasena")
        #passInput.move(950,550)
        passInput.setEchoMode(QLineEdit.Password)
        passInput.setAlignment(Qt.AlignCenter)
        passInput.setFixedSize(450,35)

        inputTextBoxesGrid.addWidget(passInput,1,2)
        inputTextBoxesGrid.addWidget(dummy.getDummyWidget(),1,3)
        inputTextBoxesGrid.addWidget(dummy.getDummyWidget(),1,0)
        #passInputLayout.setAlignment(Qt.AlignHCenter)

        self.__mainLayout.addLayout(inputTextBoxesGrid)

        btnOkLayout=QHBoxLayout()

        btnOkLayout.addWidget(dummy.getDummyWidget())

        btnOk = QPushButton('Aceptar')

        btnOkLayout.addWidget(btnOk)
        btnOkLayout.addWidget(dummy.getDummyWidget())
        #btnOk.move(850,650)
        btnOk.clicked.connect(lambda: self.comprobarUsuarioContra(usrInput.text(),passInput.text()))

        self.__mainLayout.addLayout(btnOkLayout)

        btnLayout=QHBoxLayout()

        btnLayout.addWidget(dummy.getDummyWidget())
        btn = QPushButton('Cancelar')
        btnLayout.addWidget(btn)
        btnLayout.addWidget(dummy.getDummyWidget())
        btn.clicked.connect(self.__changeToMainMenu)

        self.__mainLayout.addLayout(btnLayout)
        self.__mainLayout.setAlignment(Qt.AlignHCenter)

        self.setStyleSheet(styles.buttonStyleSheet)
        #btn.move(1000,650)

    def comprobarUsuarioContra(self,user,contra):
        print ('comprobarUsuarioContra() LogInMain')
        file = open("../Usuarios.txt","r")
        m = file.readlines()
        #     []
        # for line in file:
        #         m.append(line)
        contraRegistradas = []
        userRegistrados = []
        for i in range(0,len(m)):
            change = False
            tempUser = ""
            tempContra = ""
            for char in range(0,len(m[i]) -1 ):
                if(change == False):
                    if(m[i][char] == ':'):
                        change = True
                    else:
                        tempUser = tempUser + m[i][char]
                else:
                    tempContra = tempContra + m[i][char]
            contraRegistradas.append(tempContra)
            userRegistrados.append(tempUser)

        for i in range(0,len(userRegistrados)):
            if(userRegistrados[i] == user):
                if(contraRegistradas[i] == contra):
                    print("Usuario registrado")
                    self.__dialog.openSuccessDialog("Inicio de sesion", "Iniciando Sesion...")
                    # Funcinamiento para entrar al menu
                    self.__changeToUserMenu(user)
                    return
                else:
                    self.__dialog.openWarningDialog("Inicio de sesion", "Contrasena Incorrecta")
                return

        self.__dialog.openWarningDialog("Inicio de sesion", "Usuario Inexistente")
        file.close() 
            
    
    