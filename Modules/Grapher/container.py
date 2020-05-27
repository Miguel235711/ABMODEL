from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel
from PyQt5.QtGui import QIcon,QFont,QPixmap
#from pyqtgraph import PlotWidget, plot

import graph

class Container(QWidget):
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self):
        super(QWidget,self).__init__()
        self.__graphs=[]
        self.__initUI()

    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.__waveColors[i]))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        
    def __initWindowUILayout(self):
        self.__mainLayout=QHBoxLayout()
        self.__graphLayout=QVBoxLayout()
        self.__contectivityLayout=QVBoxLayout()
        self.__mainLayout.addLayout(self.__contectivityLayout)
        self.__mainLayout.addLayout(self.__graphLayout)
        connectionPic=QLabel() 
        connectionPic.setPixmap(QPixmap('../../Public/Images/connectionLevel.png'))
        self.__contectivityLayout.addWidget(connectionPic)
        self.setLayout(self.__mainLayout)

    def __initUI(self):
        self.__initWindowUILayout()