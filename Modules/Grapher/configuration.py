from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QHBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog,QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Configuration(QDialog):
    def __init__(self):
        super(QDialog,self).__init__(None,Qt.WindowStaysOnTopHint | Qt.WindowSystemMenuHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle('Configuracion')
        self.setWindowIcon(QIcon('../../Public/Images/cheese.jpg'))
        self.initDialogWindow()
    def initDialogWindow(self):
        #mainLayout initialization

        mainLayout=QVBoxLayout()

        #label configuration

        labelWidget=QLabel('Onda Mostrada')
        labelWidget.setAlignment(Qt.AlignCenter)
        
        #radio buttons configuration
        
        radioButtonsLayout=QHBoxLayout()
        graphRadioButton=QRadioButton('Grafica')
        radioButtonsLayout.addWidget(graphRadioButton)
        graphRadioButton.setChecked(True)
        radioButtonsLayout.addWidget(QRadioButton('Alpha'))
        radioButtonsLayout.addWidget(QRadioButton('Betha'))
        radioButtonsLayout.addWidget(QRadioButton('Delta'))
        radioButtonsLayout.addWidget(QRadioButton('Gamma'))
        #add elements to mainLayout

        mainLayout.addWidget(labelWidget)
        mainLayout.addLayout(radioButtonsLayout)

        self.setLayout(mainLayout)
