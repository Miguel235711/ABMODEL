from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *

class Pantalla(QWidget):
    def __init__(self,changeToMainMenu,changeToUserMenu):
        print ('__init__() LogInMain')
        super(QWidget,self).__init__()
        self.__changeToUserMenu=changeToUserMenu
        self.__changeToMainMenu=changeToMainMenu
        self.initUI()

    def initUI(self):
        print ('initUI() LogInMain')
        self.SetTittle()
        self.InputDialog()
        self.initWindowUILayout()

    def initWindowUILayout(self):
        print ('initWindowsUILayout() LogInMain')
        self.mainLayout=QHBoxLayout()
        self.graphLayout=QVBoxLayout()
        self.contectivityLayout=QVBoxLayout()
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        self.setLayout(self.mainLayout)

    def SetTittle(self):
        print ('SetTitle() LogInMain')
        l1 = QLabel(self)
        l1.setText("ABMODEL SYSTEM")
        l1.move(0,0)
        l1.setAlignment(Qt.AlignCenter)
        l1.resize(1920,540)
        l1.setFont(QFont('SansSerif', 50))

        l2 = QLabel(self)
        l2.setText("Iniciar Sesion")
        l2.move(0,0)
        l2.setAlignment(Qt.AlignCenter)
        l2.resize(1920,670)
        l2.setFont(QFont('SansSerif', 25))

    def InputDialog(self):
        print ('InputDialog() LogInMain')
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
        btn.clicked.connect(self.__changeToMainMenu)
        btn.move(1000,650)

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
                    self.showDialog("Inicio de sesion", "Iniciando Sesion...",QMessageBox.Information)
                    # Funcinamiento para entrar al menu
                    self.__changeToUserMenu(user)
                    return
                else:
                    self.showDialog("Inicio de sesion", "Contrasena Incorrecta",QMessageBox.Warning)
                return

        self.showDialog("Inicio de sesion", "Usuario Inexistente", QMessageBox.Warning)
        file.close() 
            
    
    def showDialog(self,titulo,textoCuerpo,icon):
        print ('showDialog() LogInMain')
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()