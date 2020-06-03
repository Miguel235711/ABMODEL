from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize,QThreadPool

import graph 
import configuration
import encephalogram

class MultiGraphContainer(QWidget):
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self,app):
        super(QWidget,self).__init__()
        self.__app=app
        self.__graphs=[]
        self.__graphLayout=QVBoxLayout()
        self.__encephalogram=encephalogram.Encephalogram()
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
        self.__configurationDialog=configuration.Configuration(self.__changeToGraphsHandler,self.__changeToEncephalogramsHandler)
        self.__recordPauseIcons=[QIcon('../../Public/Images/recordIcon.png'),QIcon('../../Public/Images/pauseIcon.png')]
    def __changeToGraphsHandler(self):
        print 'changeToGraphsHandler'
        self.__hideEncephalogram()
        self.__showGraphs()

    def __hideEncephalogram(self):
        self.__graphLayout.removeWidget(self.__encephalogram)
        self.__encephalogram.hide()

    def __changeToEncephalogramsHandler(self):
        print 'changeToEncephalogramsHandler'
        self.__hideGraphs()
        self.__showEncephalogram()

    def __showEncephalogram(self):
        self.__graphLayout.insertWidget(0,self.__encephalogram)
        self.__encephalogram.show()

    def onClickConfiguration(self):
        self.__configurationDialog.open()

    def __showGraphs(self):
        for i in range(4):
            if self.__graphs[i].getGraph().isHidden:
                self.__graphLayout.insertWidget(0,self.__graphs[i].getGraph())
                self.__graphs[i].getGraph().show()

    def __hideGraphs(self):
        for i in range(4):
            self.__graphLayout.removeWidget(self.__graphs[i].getGraph())
            self.__graphs[i].getGraph().hide()

    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        print 'initGraphsCalled'
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.__waveColors[i],self.__app))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        buttonStyleSheet="""
            QPushButton{
                background: transparent;
            }
        """
        iconSize=QSize(40,40)
        graphControlsLayout=QHBoxLayout()
        bookmarkButton=QPushButton()
        bookmarkButton.setIcon(QIcon('../../Public/Images/bookmarkIcon.png'))
        bookmarkButton.setIconSize(iconSize)
        bookmarkButton.setStyleSheet(buttonStyleSheet)
        graphControlsLayout.addWidget(bookmarkButton)
        self.__recordButton=QPushButton()
        self.__recordButton.setIcon(self.__recordPauseIcons[0])
        self.__recordButton.setIconSize(iconSize)
        self.__recordButton.clicked.connect(self.__togglePause)
        self.__recordButton.setStyleSheet(buttonStyleSheet)
        graphControlsLayout.addWidget(self.__recordButton)
        configurationButton=QPushButton()
        configurationButton.setIcon(QIcon('../../Public/Images/configurationIcon.png'))
        configurationButton.setIconSize(iconSize)
        configurationButton.setStyleSheet(buttonStyleSheet)
        configurationButton.clicked.connect(self.onClickConfiguration)
        graphControlsLayout.addWidget(configurationButton)
        self.__graphLayoutWidget=QWidget()
        self.__graphLayoutWidget.setLayout(graphControlsLayout)
        self.__graphLayout.addWidget(self.__graphLayoutWidget)
    def __setPause(self,pause):
        self.__pause=pause
        for graph in self.__graphs:
            graph.setPause(pause)
    def __getPause(self):
        return self.__graphs[0].getPause()
    def __togglePause(self):
        self.__setPause(not self.__getPause())
        self.__recordButton.setIcon(self.__recordPauseIcons[not self.__getPause()])
    def getWidget(self):
        return self.__mainWidget