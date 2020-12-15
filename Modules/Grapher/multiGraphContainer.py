# encoding: utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout,QGridLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize,QThreadPool,Qt
from random import random

import graph 
import configuration
import encephalogram

import sys
sys.path.append("../CommonWidgets")
import dummy

class MultiGraphContainer(QWidget):
    
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    __recordPauseTooltipTexts=[u'Iniciar/Continuar Grabación de Ondas',u'Detener Grabación de Ondas']
    
    def __init__(self,needsToBeReplacedWithGamma):
        print('does delta need to be replace with gamma? {}'.format(needsToBeReplacedWithGamma))
        self.__graphNames=['THETA','ALPHA','BETA','GAMMA' if needsToBeReplacedWithGamma else 'DELTA']
        self.__encephalogramNames=['Theta','Alpha','Beta','Gamma' if needsToBeReplacedWithGamma else 'Delta']
        super(QWidget,self).__init__()
        self.__graphs=[]
        self.__graphLayout=QVBoxLayout()
        self.__encephalograms={}
        for i,encephalogramName in enumerate(self.__encephalogramNames):
            self.__encephalograms[encephalogramName]=encephalogram.Encephalogram('../../Public/Images/Brain.png',self.__graphNames[i],self.__waveColors[i])
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
        self.__configurationDialog=configuration.Configuration(self.__changeToGraphsHandler,self.__changeToEncephalogramsHandler,needsToBeReplacedWithGamma)
        self.__recordPauseIcons=[QIcon('../../Public/Images/recordIcon.png'),QIcon('../../Public/Images/pauseIcon.png')]
    def __changeToGraphsHandler(self,key):
        #print 'changeToGraphsHandler'
        self.__hideEncephalogram(key)
        self.__showGraphs()

    def __hideEncephalogram(self,key):
        if key in self.__encephalograms:
            self.__graphLayout.removeWidget(self.__encephalograms[key])
            self.__encephalograms[key].hide()

    def __changeToEncephalogramsHandler(self,lastKey,key):
        #print 'changeToEncephalogramsHandler'
        if lastKey!='':
            self.__hideEncephalogram(lastKey)
        self.__hideGraphs()
        self.__showEncephalogram(key)

    def __showEncephalogram(self,key):
         if key in self.__encephalograms:
            self.__graphLayout.insertWidget(0,self.__encephalograms[key])
            self.__encephalograms[key].show()

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

    def initGraphsAndEncephalograms(self,graphData,encephalogramData):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        #print 'initGraphsCalled\n\n\n'
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in graphData ],[pair[1][i] for pair in graphData],self.__waveColors[i],self.__graphNames[i]))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        for i,encephalogramName in enumerate(self.__encephalogramNames): 
            self.__encephalograms[encephalogramName].initEncephalogram(encephalogramData[i])
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
        bookmarkButton.setToolTip(u'Agregar Nota a Gráfica')
        bookmarkButton.setEnabled(False)
        bookmarkButton.setFixedSize(iconSize)
        #graphControlsLayout.addWidget(bookmarkButton)
        self.__recordButton=QPushButton()
        self.__recordButton.setIcon(self.__recordPauseIcons[0])
        self.__recordButton.setIconSize(iconSize)
        self.__recordButton.clicked.connect(self.__togglePause)
        self.__recordButton.setStyleSheet(buttonStyleSheet)
        self.__recordButton.setToolTip(self.__recordPauseTooltipTexts[0])
        self.__recordButton.setFixedSize(iconSize)
        #graphControlsLayout.addWidget(self.__recordButton)
        bookmarkAndRecordButtonLayout=QHBoxLayout()
        bookmarkAndRecordButtonLayout.addWidget(dummy.getDummyWidget())
        bookmarkAndRecordButtonLayout.addWidget(bookmarkButton)
        bookmarkAndRecordButtonLayout.addWidget(self.__recordButton)
        bookmarkAndRecordButtonLayout.setSpacing(0)
        graphControlsLayout.addLayout(bookmarkAndRecordButtonLayout)
        configurationButton=QPushButton()
        configurationButton.setIcon(QIcon('../../Public/Images/configurationIcon.png'))
        configurationButton.setIconSize(iconSize)
        configurationButton.setStyleSheet(buttonStyleSheet)
        configurationButton.clicked.connect(self.onClickConfiguration)
        configurationButton.setToolTip(u'Cambiar Tipo de Graficación')
        configurationButton.setFixedSize(iconSize)
        configurationLayout=QHBoxLayout()
        configurationLayout.addWidget(dummy.getDummyWidget())
        configurationLayout.addWidget(configurationButton)
        graphControlsLayout.addLayout(configurationLayout)
        self.__graphLayoutWidget=QWidget()
        self.__graphLayoutWidget.setLayout(graphControlsLayout)
        self.__graphLayout.addWidget(self.__graphLayoutWidget)
    def __setPause(self,pause):
        self.__pause=pause
        for graph in self.__graphs:
            graph.setPause(pause)
        for encephalogram in self.__encephalograms.values():
            encephalogram.setPause(pause)
    def __getPause(self):
        return self.__graphs[0].getPause()
    def __togglePause(self):
        self.__setPause(not self.__getPause())
        self.__recordButton.setIcon(self.__recordPauseIcons[not self.__getPause()])
        self.__recordButton.setToolTip(self.__recordPauseTooltipTexts[not self.__getPause()])
    def getWidget(self):
        return self.__mainWidget