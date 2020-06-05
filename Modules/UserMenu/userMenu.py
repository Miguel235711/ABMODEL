from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *

class Pantalla(QWidget):
    def __init__(self,changeToMainMenu,changeToGrapher,username):
        super(QWidget,self).__init__()
        print 'user menu received',username
        self.__changeToMainMenu=changeToMainMenu
        self.__changeToGrapher=changeToGrapher
        self.__username=username
        self.initUI()
    def initUI(self):
        self.InputDialog()
    def __getFile(self):
        fileInfo=QFileDialog.getOpenFileName(self,"Selecciona Archivo","","Files (*.csv)")
        return(fileInfo[0])
    def __openFile(self):
        filePath=self.__getFile()
        tokens=filePath.split('.')
        if not tokens or tokens[len(tokens)-1]=='csv':
            self.__changeToGrapher(self.__username,filePath)
        else:
            self.showDialog("Error", "El archivo seleccionado no tiene una extension valida, seleccione un archivo .csv" ,QMessageBox.Information)
    def InputDialog(self):
        inputLayout=QVBoxLayout()
        self.setLayout(inputLayout)

        title=QLabel("ABMODEL SYSTEM")
        title.resize(1920,540)
        title.setFont(QFont('SansSerif', 50))
        title.setAlignment(Qt.AlignCenter)

        inputLayout.addWidget(title)
        welcome=QLabel("Bievenido: "+str(self.__username))
        welcome.resize(1920,670)
        welcome.setFont(QFont('SansSerif', 25))
        welcome.setAlignment(Qt.AlignCenter)

        inputLayout.addWidget(welcome)

        QPushButton('Nuevo Archivo')
        newFileButton=QPushButton('Nuevo Archivo')
        newFileButton.setEnabled(False)
        inputLayout.addWidget(newFileButton)
        
        openFileButton=QPushButton('Abrir Archivo')
        openFileButton.clicked.connect(self.__openFile)
        inputLayout.addWidget(openFileButton)

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
    def showDialog(self,titulo,textoCuerpo,icon):
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()