from PyQt5.QtWidgets import QWidget,QGraphicsProxyWidget,QPushButton,QLabel,QHBoxLayout
from pyqtgraph import PlotWidget,mkPen,setConfigOption,TextItem
from QtCore import QObject,pyqtSignal,QRectF,Qt
from time import sleep
from PyQt5 import QtCore
from threading import Thread

class Graph():
    class Worker(QObject):
        readyForNextPoint = pyqtSignal()
        def __init__(self):
            super(QObject,self).__init__()
            self.__continue=True
            self.__pause=True
        def __changeFlagToFalse(self):
            self.__continue=False
        def startThread(self,timePoints,app):
            #print 'inside Function()'
            self.__timePoints=timePoints
            self.__thread=Thread(target=self.__func)
            app.aboutToQuit.connect(self.__changeFlagToFalse)
            self.__thread.start()
        def __func(self):
            #print 'inside __func()'
            lastTime=0
            for time in self.__timePoints:
                while(self.__pause):
                    if not self.__continue:
                        return
                    sleep(1)
                if not self.__continue:
                    return
                sleep(time-lastTime)
                self.readyForNextPoint.emit()
                lastTime=time
        def setPause(self,pause):
            self.__pause=pause
        def getPause(self):
            return self.__pause
    xDifLimit=8
    def mouseClick(self,event):
        print event
    def __init__(self,timePoints,wavePoints,waveColor,app,name):
        setConfigOption('background',(230,230,230))
        setConfigOption('foreground',(0,0,0))
        self.__app=app
        mainLayout=QHBoxLayout()
        self.__mainWidget=QWidget()
        self.__mainWidget.setLayout(mainLayout)
        self.__graph=PlotWidget()
        mainLayout.addWidget(self.__graph)
        label=QLabel(name)
        label.setFixedSize(50,30)
        label.setAlignment(Qt.AlignCenter)
        backgroundColor="background:rgb"+"("+str(waveColor[0])+","+str(waveColor[1])+","+str(waveColor[2])+");"
        print backgroundColor
        label.setStyleSheet("""
            color:black;
            font: bold;"""+
            backgroundColor+
        """
            height: 30px;
            text-align:center;
        """)
        mainLayout.addWidget(label)
        self.__graph.setMouseTracking(True)
        self.__graph.scene().sigMouseClicked.connect(self.mouseClick)
        self.__graph.setLabel('bottom','Tiempo',units='s')
        #testing add item to plot widget
            #proxy = QGraphicsProxyWidget()
            #proxy.setGeometry(QRectF(0,0,1,1))
            #button=QPushButton('button')
            #button.setGeometry(0,0,1,1)
            #proxy.setWidget(button)
            #self.__graph.addItem(proxy,y=0)
            #self.__graph.addItem(proxy,y=10)
        #testing adding textitem
        #self.__graph.addItem(TextItem())
        #self.__graph.setXRange(0,8)
        self.__timePoints=timePoints
        self.__wavePoints=wavePoints
        self.__waveColor=waveColor
        self.__timePointsProgressive,self.__wavePointsProgressive=[],[]
        self.__i=0
        ##times=[pair[0] for pair in data ]
        ##firstWave=[pair[1][0] for pair in data]
        ##self.graphWidget.plot(times,firstWave)
    @QtCore.pyqtSlot()
    def setPause(self,pause):
        self.__worker.setPause(pause)
    def getPause(self):
        return self.__worker.getPause()
    def __plotNextPoint(self):
        #print 'inside __realTimePlotting()'
        #sleep(self.__timePoints[i]-lastTime)
        self.__timePointsProgressive.append(self.__timePoints[self.__i])
        self.__wavePointsProgressive.append(self.__wavePoints[self.__i])
        last =self.__timePointsProgressive[len(self.__timePointsProgressive)-1]
        first = self.__timePointsProgressive[0]
        x0= first if last - first <= self.xDifLimit else last - self.xDifLimit
        x1= x0 + self.xDifLimit
        print(x0,x1)
        if self.__i&1:
            self.__graph.plot(self.__timePointsProgressive,self.__wavePointsProgressive,pen=mkPen(color=self.__waveColor,width=3))
            self.__graph.setXRange(x0,x1)
        self.__i+=1
    def plotGraph(self):
        #worker = self.Worker(self.__realTimePlotting)
        #threadPool.start(worker)
        #self.__realTimeGraphThread = Thread(target=self.realTimePlotting)
        #self.__realTimeGraphThread.start()
        #print 'inside plotGraph()'
        self.__worker = self.Worker()
        self.__worker.readyForNextPoint.connect(self.__plotNextPoint)
        self.__worker.startThread(self.__timePoints,self.__app)
        #!self.__plottingThread = self.__QThreadImplementation(self.__realTimePlotting)
        #!self.__plottingThread.start()
    def getGraph(self):
        return self.__mainWidget