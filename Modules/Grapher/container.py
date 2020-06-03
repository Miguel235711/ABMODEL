from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
#from pyqtgraph import PlotWidget, plot

import multiGraphContainer
import menu
import userInfo

class Container(QWidget):
    def __init__(self,app):
        super(QWidget,self).__init__()
        self.__dialogWindow=menu.Menu()
        self.__graphsWidget=multiGraphContainer.MultiGraphContainer(app)
        self.__initUI()
    def initGraphs(self,data):
        self.__graphsWidget.initGraphs(data)

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
        connectionPic=QLabel() 
        connectionPic.setPixmap(QPixmap('../../Public/Images/connectionLevel.png'))
        self.__mainLayout.addWidget(connectionPic)
        self.__mainLayout.addWidget(self.__graphsWidget.getWidget())
        
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
        QPushButton:hover {
            background: rgb(230,230,230)
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