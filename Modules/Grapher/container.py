# encoding: utf-8
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QFont,QPixmap
#from pyqtgraph import PlotWidget, plot

import multiGraphContainer
import menu
import userInfo

import sys
sys.path.append("../CommonWidgets")
import styles

class Container(QWidget):
    def __init__(self,changeToUserMenu,username,filePath,needsToBeReplacedWithGamma):
        super(QWidget,self).__init__()
        self.__username=username
        self.__filePath=filePath
        self.__dialogWindow=menu.Menu(changeToUserMenu,username,filePath)
        self.__graphsWidget=multiGraphContainer.MultiGraphContainer(needsToBeReplacedWithGamma)
        self.__initUI()
    def initGraphsAndEncephalograms(self,graphData,encephalogramData):
        self.__graphsWidget.initGraphsAndEncephalograms(graphData,encephalogramData)

    def onClickMenuButton(self):
        #print 'Menu Button Clicked'
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
        userInfoWidgetInstance=userInfo.UserInfo(self.__username,self.__filePath)
        userInfoWidgetInstance.setSizePolicy(spLeft)
        self.__menuBarLayout.addWidget(userInfoWidgetInstance)

        #menu button
        spRight=QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        spRight.setHorizontalStretch(1)
        self.__menuButton=QPushButton(u'Menú')
        self.__menuButton.setSizePolicy(spRight)
        self.__menuButton.setStyleSheet(styles.buttonStyleSheet)
        self.__menuButton.clicked.connect(self.onClickMenuButton)
        self.__menuButton.setToolTip(u'Abrir Menú')
        self.__menuBarLayout.addWidget(self.__menuButton)

        #adding sublayouts to globaLayout

        self.__globalLayout.addLayout(self.__menuBarLayout)
        self.__globalLayout.addLayout(self.__mainLayout)

        #set globaLayout to container

        self.setLayout(self.__globalLayout)
    def __initUI(self):
        self.__initWindowUILayout()
        self.__dialogWindow.initDialogWindow()