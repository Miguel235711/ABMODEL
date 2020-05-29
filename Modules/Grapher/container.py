from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
#from pyqtgraph import PlotWidget, plot

import graph
import menu
import userInfo

class Container(QWidget):
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self):
        super(QWidget,self).__init__()
        self.__graphs=[]
        self.__dialogWindow=menu.Menu()
        self.__initUI()

    def initGraphs(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        for i in range(4):
            self.__graphs.append(graph.Graph([pair[0] for pair in data ],[pair[1][i] for pair in data],self.__waveColors[i]))
            self.__graphs[i].plotGraph()
            self.__graphLayout.addWidget(self.__graphs[i].getGraph())
        
    def onClickMenuButton(self):
        print 'Menu Button Clicked'
        self.__dialogWindow.open()
    def __initWindowUILayout(self):
        #root layout
        
        self.__globalLayout=QVBoxLayout()
        
        #main layout

        self.__mainLayout=QHBoxLayout()
        self.__graphLayout=QVBoxLayout()
        self.__contectivityLayout=QVBoxLayout()
        self.__mainLayout.addLayout(self.__contectivityLayout)
        self.__mainLayout.addLayout(self.__graphLayout)
        connectionPic=QLabel() 
        connectionPic.setPixmap(QPixmap('../../Public/Images/connectionLevel.png'))
        self.__contectivityLayout.addWidget(connectionPic)
        
        #menu bar layout
        self.__menuBarLayout=QHBoxLayout()
        
        #user info
        spLeft=QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        spLeft.setHorizontalStretch(3)
        userInfoWidgetInstance=userInfo.UserInfo()
        userInfoWidgetInstance.setSizePolicy(spLeft)
        self.__menuBarLayout.addWidget(userInfoWidgetInstance)

        #menu button
        spRight=QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        spRight.setHorizontalStretch(1)
        self.__menuButton=QPushButton("Menu")
        self.__menuButton.setSizePolicy(spRight)
        self.__menuButton.setStyleSheet(
        """
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
        """)
        self.__menuButton.clicked.connect(self.onClickMenuButton)
        self.__menuButton.setToolTip("Abrir Menu")
        self.__menuBarLayout.addWidget(self.__menuButton)

        #adding sublayouts to globaLayout

        self.__globalLayout.addLayout(self.__menuBarLayout)
        self.__globalLayout.addLayout(self.__mainLayout)

        #set globaLayout to container

        self.setLayout(self.__globalLayout)
    def __initUI(self):
        self.__initWindowUILayout()
        self.__dialogWindow.initDialogWindow()