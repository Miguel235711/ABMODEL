from PyQt5.QtWidgets import QWidget,QToolTip,QStatusBar,QLabel,QMessageBox,QHBoxLayout
from PyQt5.QtGui import QFont,QIcon,QPixmap

class State(QWidget):
    class __state:
        def __init__(self,colorConfig,icon,label):
            self.colorConfig=colorConfig
            self.icon=icon
            self.label=label
    __states=[
        __state('color: green',None,'Conectado'),
        __state('color: red',None,'Desconectado')
    ]
    __iconsAlreadyLoaded=False


    def __init__(self):
        super(QWidget,self).__init__()

        if not State.__iconsAlreadyLoaded:
            #load icons
            print('load icons')
            State.__states[0].icon=QPixmap("../../Public/Images/connectedIcon.png")
            State.__states[0].icon=State.__states[0].icon.scaledToWidth(30)
            State.__states[1].icon=QPixmap("../../Public/Images/disconnectedIcon.png")
            State.__states[1].icon=State.__states[1].icon.scaledToWidth(30)
            State.__iconsAlreadyLoaded=True
        
        #boolean for connection state

        self.__isConnected=False

        #instatiate widgets

        self.__container=QHBoxLayout()
        self.__connectionImage=QLabel()
        self.__connectionLabel=QLabel()

        #update state

        self.__updateState()

        #add widgets to container

        self.__container.addWidget(QLabel("Estado: "))
        self.__container.addWidget(self.__connectionLabel)
        self.__container.addWidget(self.__connectionImage)

        #set container as layout

        self.setLayout(self.__container)
        
    def __updateState(self):
        stateIndex = 0 if self.__isConnected else 1 
        self.__connectionLabel.setText(State.__states[stateIndex].label)
        self.__connectionLabel.setStyleSheet(State.__states[stateIndex].colorConfig)
        self.__connectionImage.setPixmap(State.__states[stateIndex].icon)

    def setConnectionState(self,isConnected):
        if isConnected != self.__isConnected:
            self.__isConnected=isConnected
            #change color,icon and label
            self.__updateState()

    def getConnectionState(self):
        return self.__isConnected
