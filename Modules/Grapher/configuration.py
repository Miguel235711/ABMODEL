from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QHBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog,QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from functools import partial

class Configuration(QDialog):
    __modes=['Grafica','Alpha','Betha','Delta','Gamma']
    def __init__(self,changeToGraphHandler,changeToEncephalogramHandler):
        super(QDialog,self).__init__(None,Qt.WindowStaysOnTopHint | Qt.WindowSystemMenuHint| Qt.WindowCloseButtonHint)
        self.setWindowTitle('Configuracion')
        self.setWindowIcon(QIcon('../../Public/Images/cheese.jpg'))
        self.initDialogWindow()
        self.__changeToGraphHandler=changeToGraphHandler
        self.__changeToEncephalogramHandler=changeToEncephalogramHandler
    def __selectMode(self,key):
        print 'key: ',key
        if key != self.__currentTrueRadioButtonKey:
            #make changes
            if key=='Grafica':
                self.__changeToGraphHandler()
            else:
                self.__changeToEncephalogramHandler()
            self.__currentTrueRadioButtonKey=key
    def initDialogWindow(self):
        #mainLayout initialization

        mainLayout=QVBoxLayout()

        #label configuration

        labelWidget=QLabel('Onda Mostrada')
        labelWidget.setAlignment(Qt.AlignCenter)
        
        #radio buttons configuration
        radioButtonsLayout=QHBoxLayout()
        for i,mode in enumerate(self.__modes):
            radioButton=QRadioButton(mode)
            radioButton.clicked.connect(partial(self.__selectMode,mode))
            radioButtonsLayout.addWidget(radioButton)
            if i==0:
                radioButton.setChecked(True)
                self.__currentTrueRadioButtonKey=mode
        #add elements to mainLayout
        mainLayout.addWidget(labelWidget)
        mainLayout.addLayout(radioButtonsLayout)

        self.setLayout(mainLayout)
