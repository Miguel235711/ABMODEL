from PyQt5.QtWidgets import QWidget,QGraphicsProxyWidget,QPushButton,QLabel,QHBoxLayout
from pyqtgraph import PlotWidget,mkPen,setConfigOption,TextItem
from QtCore import QRectF,Qt
from PyQt5 import QtCore

from threadWorker import Worker

class Graph():
    xDifLimit=8
    def mouseClick(self,event):
        print event
    def __init__(self,timePoints,wavePoints,waveColor,app,name):
        setConfigOption('background',(230,230,230))
        setConfigOption('foreground',(0,0,0))
        self.__mkPen=mkPen(color=waveColor,width=3)
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
            backgroundColor)
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
    def __recalculateX0X1(self,lastTime):
        first = self.__firstTime
        x0= first if lastTime - first <= self.xDifLimit else lastTime - self.xDifLimit
        x1= x0 + self.xDifLimit
        self.__graph.setXRange(x0,x1)
        print(x0,x1)
    def __plotNextPoint(self):
        #print 'inside __realTimePlotting()'
        #sleep(self.__timePoints[i]-lastTime)
        if len(self.__timePointsProgressive) >= 10:
                self.__timePointsProgressive.pop(0)
                self.__wavePointsProgressive.pop(0)
        if self.__i < len(self.__timePoints):
            self.__timePointsProgressive.append(self.__timePoints[self.__i])
            self.__wavePointsProgressive.append(self.__wavePoints[self.__i])
        else:
            self.__timePointsProgressive.append(self.__timePointsProgressive[len(self.__timePointsProgressive)-1]+0.250)
            self.__wavePointsProgressive.append(0)
        if self.__i&1:
            self.__graph.plot(self.__timePointsProgressive,self.__wavePointsProgressive,pen=self.__mkPen)
            self.__recalculateX0X1(self.__timePointsProgressive[len(self.__timePointsProgressive)-1])
        self.__i+=1
        
    def plotGraph(self):
        #worker = self.Worker(self.__realTimePlotting)
        #threadPool.start(worker)
        #self.__realTimeGraphThread = Thread(target=self.realTimePlotting)
        #self.__realTimeGraphThread.start()
        #print 'inside plotGraph()'
        self.__worker = Worker()
        self.__worker.readyForNextPoint.connect(self.__plotNextPoint)
        self.__firstTime=self.__timePoints[0]
        self.__worker.startThread(self.__timePoints,self.__app)
        #!self.__plottingThread = self.__QThreadImplementation(self.__realTimePlotting)
        #!self.__plottingThread.start()
    def getGraph(self):
        return self.__mainWidget