from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *

class Pantalla(QWidget):
    def __init__(self,changeToMainMenu,username):
        super(QWidget,self).__init__()
        print 'user menu received',username
        self.__changeToMainMenu=changeToMainMenu
        self.__username=username
        self.initUI()
    def initUI(self):
        self.InputDialog()
    def InputDialog(self):
        inputLayout=QVBoxLayout()
        self.setLayout(inputLayout)

        title=QLabel("ABMODEL SYSTEM")
        title.resize(1920,540)
        title.setFont(QFont('SansSerif', 50))
        title.setAlignment(Qt.AlignCenter)

        inputLayout.addWidget(title)
        welcome=QLabel("Bievenido: "+self.__username)
        welcome.resize(1920,670)
        welcome.setFont(QFont('SansSerif', 25))
        welcome.setAlignment(Qt.AlignCenter)

        inputLayout.addWidget(welcome)

        inputLayout.addWidget(QPushButton('Nuevo Archivo'))

        inputLayout.addWidget(QPushButton('Abrir Archivo'))

        btn = QPushButton('Cerrar Sesion',self)
        btn.clicked.connect(self.__changeToMainMenu)
        inputLayout.addWidget(btn)

        self.setStyleSheet("""
        QPushButton{
            border-radius:20px;
            background-color:white;
            padding: 10px;
            border-width:1.5px;
            border-color:black;
            border-style: outset;
            font: bold 30px;
            margin-top:20px;
            margin-bottom:20px;
            margin-right:80px;
        }
        QPushButton:hover {
            background: rgb(230,230,230)
        }
        """)
        #btn.move(1000,600)

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
