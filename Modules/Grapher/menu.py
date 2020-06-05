from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Menu(QDialog):
    def __init__(self):
        super(QDialog,self).__init__(None,Qt.WindowStaysOnTopHint | Qt.WindowSystemMenuHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle('Menu')
        self.setWindowIcon(QIcon('../../Public/Images/cheese.jpg'))

    def __getFile(self):
        fileInfo=QFileDialog.getOpenFileName(self,"Selecciona Archivo","","Files (*.csv)")
        self.__filePathLabel.setText(fileInfo[0])
    def initDialogWindow(self):
        mainLayout=QVBoxLayout()

        #initialize sub-layouts
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

        fileNameLayout=QHBoxLayout()
        pacientLayout=QHBoxLayout()
        fileDateLayout=QHBoxLayout()
        filePathLayout=QHBoxLayout()
        saveAndreturnButtonLayout=QHBoxLayout()

        #add contents to sub-layouts

        #fileName

        fileNameLayout.addWidget(QLabel('Nombre del Archivo: '))
        fileNameLayout.addWidget(QLineEdit())

        #pacient

        pacientLayout.addWidget(QLabel('Paciente: '))
        pacientLayout.addWidget(QLineEdit())

        #fileDate

        fileDateLayout.addWidget(QLabel('Fecha del Archivo: '))
        fileDateLayout.addWidget(QLabel('30/02/2020'))

        #filePath

        filePathLayout.addWidget(QLabel('Direccion del Archivo: '))
        self.__filePathLabel=QLabel('C:\Users\Torybio\Documents\MonitoreoAB')
        filePathLayout.addWidget(self.__filePathLabel)
        selectFileButton=QPushButton('...')
        selectFileButton.clicked.connect(self.__getFile)
        filePathLayout.addWidget(selectFileButton)

        #saveAndreturnButton

        saveButton=QPushButton('Guardar')
        returnButton=QPushButton('Regresar')
        saveAndreturnButtonLayout.addWidget(saveButton)
        saveAndreturnButtonLayout.addWidget(returnButton)
        #saveAndreturnButtonLayout.setAlignment(saveButton,Qt.AlignHCenter)
        #saveAndreturnButtonLayout.setAlignment(returnButton,Qt.AlignHCenter)
        #exitButton

        exitButton=QPushButton('Salir')
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