from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from datetime import datetime
import sys
sys.path.append("../CommonWidgets")
import styles

class Menu(QDialog):
    def __init__(self,changeToUserMenu,username,filePath):
        super(QDialog,self).__init__(None,Qt.WindowStaysOnTopHint | Qt.WindowSystemMenuHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle('Menu')
        self.setWindowIcon(QIcon('../../Public/Images/cheese.jpg'))
        self.__changeToUserMenu=changeToUserMenu
        self.__username=username
        self.__filePath=filePath

    def __getFile(self):
        fileInfo=QFileDialog.getOpenFileName(self,"Selecciona Archivo","","Files (*.csv)")
        self.__filePathLabel.setText(fileInfo[0])
    def __exit(self):
        self.__changeToUserMenu(self.__username)
        self.close()
    def initDialogWindow(self):
        mainLayout=QVBoxLayout()

        #initialize sub-layouts
        self.setStyleSheet(styles.buttonStyleSheet)

        fileNameLayout=QHBoxLayout()
        pacientLayout=QHBoxLayout()
        fileDateLayout=QHBoxLayout()
        filePathLayout=QHBoxLayout()
        saveAndreturnButtonLayout=QHBoxLayout()

        #add contents to sub-layouts

        #fileName

        fileNameLayout.addWidget(QLabel('Nombre del Archivo: '))
        inputFile=QLineEdit()
        inputFile.setEnabled(False)
        fileNameLayout.addWidget(inputFile)

        #pacient

        pacientLayout.addWidget(QLabel('Paciente: '))
        inputPacient=QLineEdit()
        inputPacient.setEnabled(False)
        pacientLayout.addWidget(inputPacient)

        #fileDate

        fileDateLayout.addWidget(QLabel('Fecha del Archivo: '))
        fileDateLayout.addWidget(QLabel(datetime.today().strftime('%d-%m-%Y')))

        #filePath

        filePathLayout.addWidget(QLabel('Direccion del Archivo: '))
        beg=max(0,len(self.__filePath)-160)
        self.__filePathLabel=QLabel(('...' if beg>0 else '')+self.__filePath[beg:])
        filePathLayout.addWidget(self.__filePathLabel)
        selectFileButton=QPushButton('...')
        selectFileButton.clicked.connect(self.__getFile)
        selectFileButton.setEnabled(False)
        filePathLayout.addWidget(selectFileButton)

        #saveAndreturnButton

        saveButton=QPushButton('Guardar')
        saveButton.setEnabled(False)
        returnButton=QPushButton('Regresar')
        saveAndreturnButtonLayout.addWidget(saveButton)
        returnButton.clicked.connect(self.close)
        saveAndreturnButtonLayout.addWidget(returnButton)
        #saveAndreturnButtonLayout.setAlignment(saveButton,Qt.AlignHCenter)
        #saveAndreturnButtonLayout.setAlignment(returnButton,Qt.AlignHCenter)
        #exitButton

        exitButton=QPushButton('Salir')
        exitButton.clicked.connect(self.__exit)
        #exitButton.setAlignment()

        #adding sublayouts to mainLayout

        mainLayout.addLayout(fileNameLayout)
        mainLayout.addLayout(pacientLayout)
        mainLayout.addLayout(fileDateLayout)
        mainLayout.addLayout(filePathLayout)
        mainLayout.addLayout(saveAndreturnButtonLayout)
        mainLayout.addWidget(exitButton)
        mainLayout.setAlignment(exitButton,Qt.AlignHCenter)
        self.setLayout(mainLayout)