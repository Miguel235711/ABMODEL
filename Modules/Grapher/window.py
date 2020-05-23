from PyQt5.QtWidgets import QWidget,QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip
from PyQt5.QtGui import QIcon,QFont
#from pyqtgraph import PlotWidget, plot

import graph

class Window(QWidget):
    waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self,title,iconPath):
        super(QWidget,self).__init__()
        self.title=title
        self.iconPath=iconPath
        self.graphs=[]
        self.initUI()
    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        for i in range(4):
            self.graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.waveColors[i]))
            self.graphs[i].plotGraph()
            self.graphLayout.addWidget(self.graphs[i].getGraph())
        #self.graph0.printData()
    def initWindowUIMetaData(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconPath))
    def initWindowUILayout(self):
        self.mainLayout=QHBoxLayout()
        self.graphLayout=QVBoxLayout()
        self.contectivityLayout=QVBoxLayout()
        btn0 = QPushButton('Button0')
        self.mainLayout.addLayout(self.contectivityLayout)
        self.mainLayout.addLayout(self.graphLayout)
        self.contectivityLayout.addWidget(btn0)
        self.setLayout(self.mainLayout)

    def initUI(self):
        self.initWindowUIMetaData()
        self.initWindowUILayout()
        self.show()
        self.resize(1800,900)
        self.move(0,0)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()