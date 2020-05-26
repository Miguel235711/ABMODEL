from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel
from PyQt5.QtGui import QIcon,QFont,QPixmap
#from pyqtgraph import PlotWidget, plot

import graph

class Container(QWidget):
    waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self):
        super(QWidget,self).__init__()
        self.graphs=[]
        self.initUI()

    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        for i in range(4):
            self.graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.waveColors[i]))
            self.graphs[i].plotGraph()
            self.graphLayout.addWidget(self.graphs[i].getGraph())
        
    def initWindowUILayout(self):
        self.mainLayout=QHBoxLayout()
        self.graphLayout=QVBoxLayout()
        self.contectivityLayout=QVBoxLayout()
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        connectionPic=QLabel() 
        connectionPic.setPixmap(QPixmap('../../Public/Images/connectionLevel.png'))
        self.contectivityLayout.addWidget(connectionPic)
        self.setLayout(self.mainLayout)

    def initUI(self):
        self.initWindowUILayout()