from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog

import graph

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
    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        print 'initGraphsCalled'
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.__waveColors[i]))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        graphControlsLayout=QHBoxLayout()
        graphControlsLayout.addWidget(QPushButton('a'))
        graphControlsLayout.addWidget(QPushButton('b'))
        graphControlsLayout.addWidget(QPushButton('b'))
        self.__graphLayout.addLayout(graphControlsLayout)

    def getWidget(self):
        return self.__mainWidget