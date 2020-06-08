from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import *
import sys
sys.path.append("../CommonWidgets")
import styles

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
        print fileInfo
        return (True if fileInfo[1]!='' else False,fileInfo[0])
    def __openFile(self):
        filePathAns=self.__getFile()
        tokens=filePathAns[1].split('.')
        if not tokens or tokens[len(tokens)-1]=='csv':
            self.__changeToGrapher(self.__username,filePathAns[1])
        elif filePathAns[0]:
            self.showDialog("Error", "El archivo seleccionado no tiene una extension valida, seleccione un archivo .csv" ,QMessageBox.Information)
    def InputDialog(self):
        inputLayout=QVBoxLayout()
        self.setLayout(inputLayout)

        title=QLabel("ABMODEL SYSTEM")
        title.resize(1920,540)
        title.setFont(QFont('SansSerif', 50))
        title.setAlignment(Qt.AlignHCenter)

        inputLayout.addWidget(title,Qt.AlignHCenter)
        welcome=QLabel("Bievenido: "+str(self.__username))
        welcome.resize(1920,670)
        welcome.setFont(QFont('SansSerif', 25))
        welcome.setAlignment(Qt.AlignHCenter)

        inputLayout.addWidget(welcome,Qt.AlignHCenter)

        newFileButton=QPushButton('Nuevo Archivo')
        newFileButton.setEnabled(False)
        inputLayout.addWidget(newFileButton,Qt.AlignHCenter)
        
        openFileButton=QPushButton('Abrir Archivo')
        openFileButton.clicked.connect(self.__openFile)
        inputLayout.addWidget(openFileButton,Qt.AlignHCenter)

        btn = QPushButton('Cerrar Sesion',self)
        btn.clicked.connect(self.__changeToMainMenu)
        inputLayout.addWidget(btn,Qt.AlignHCenter)
        inputLayout.setAlignment(Qt.AlignHCenter)
        self.setStyleSheet(styles.buttonStyleSheet)
        #btn.move(1000,600)
    def showDialog(self,titulo,textoCuerpo,icon):
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        x = dialog.exec_()