from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap

import graph 
import configuration

class MultiGraphContainer(QWidget):
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self):
        super(QWidget,self).__init__()
        self.__graphs=[]
        self.__graphLayout=QVBoxLayout()
        self.__mainWidget=QWidget(self)
        self.__mainWidget.setLayout(self.__graphLayout)
        self.__mainWidget.setObjectName('mainWidget')
        self.__mainWidget.setStyleSheet(
        """
            QWidget#mainWidget
            {
                border-radius:20px;
                background-color:white;
                border-width:1.5px;
                border-color:black;
                border-style: outset;
            }
        """
        )
        self.__configurationDialog=configuration.Configuration()
    def onClickConfiguration(self):
        self.__configurationDialog.open()
    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        print 'initGraphsCalled'
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.__waveColors[i]))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        buttonStyleSheet="""
            QPushButton{
                background: transparent;
            }
        """

        graphControlsLayout=QHBoxLayout()
        bookmarkButton=QPushButton()
        bookmarkButton.setIcon(QIcon('../../Public/Images/bookmarkIcon.png'))
        bookmarkButton.setStyleSheet(buttonStyleSheet)
        graphControlsLayout.addWidget(bookmarkButton)
        recordButton=QPushButton()
        recordButton.setIcon(QIcon(QPixmap('../../Public/Images/recordIcon.png')))
        recordButton.setStyleSheet(buttonStyleSheet)
        graphControlsLayout.addWidget(recordButton)
        configurationButton=QPushButton()
        configurationButton.setIcon(QIcon(QPixmap('../../Public/Images/configurationIcon.png')))
        configurationButton.setStyleSheet(buttonStyleSheet)
        configurationButton.clicked.connect(self.onClickConfiguration)
        graphControlsLayout.addWidget(configurationButton)
        self.__graphLayout.addLayout(graphControlsLayout)

    def getWidget(self):
        return self.__mainWidget