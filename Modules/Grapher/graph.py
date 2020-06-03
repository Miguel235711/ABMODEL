from PyQt5.QtWidgets import QWidget
from pyqtgraph import PlotWidget,mkPen,setConfigOption
from QtCore import QObject,pyqtSignal
from time import sleep
from PyQt5 import QtCore
from threading import Thread

class Graph():
    class Worker(QObject):
        readyForNextPoint = pyqtSignal()
        #def __init__(self):
        #    super(QObject,self).__init__()
        def startThread(self,timePoints):
            #print 'inside Function()'
            self.__timePoints=timePoints
            Thread(target=self.__func).start()
        def __func(self):
            #print 'inside __func()'
            lastTime=0
            for time in self.__timePoints:
                sleep(time-lastTime)
                self.readyForNextPoint.emit()
                lastTime=time
    def __init__(self,timePoints,wavePoints,waveColor):
        setConfigOption('background',(230,230,230))
        setConfigOption('foreground',(0,0,0))
        self.__graph=PlotWidget()
        self.__graph.setXRange(0,8)
        self.__timePoints=timePoints
        self.__wavePoints=wavePoints
        self.__waveColor=waveColor
        self.__timePointsProgressive,self.__wavePointsProgressive=[],[]
        self.__i=0
        ##times=[pair[0] for pair in data ]
        ##firstWave=[pair[1][0] for pair in data]
        ##self.graphWidget.plot(times,firstWave)
    @QtCore.pyqtSlot()
    def __plotNextPoint(self):
        #print 'inside __realTimePlotting()'
        #sleep(self.__timePoints[i]-lastTime)
        self.__timePointsProgressive.append(self.__timePoints[self.__i])
        self.__wavePointsProgressive.append(self.__wavePoints[self.__i])
        self.__graph.plot(self.__timePointsProgressive,self.__wavePointsProgressive,pen=mkPen(color=self.__waveColor,width=3))
        self.__i+=1
    def plotGraph(self):
        #worker = self.Worker(self.__realTimePlotting)
        #threadPool.start(worker)
        #self.__realTimeGraphThread = Thread(target=self.realTimePlotting)
        #self.__realTimeGraphThread.start()
        #print 'inside plotGraph()'
        self.__worker = self.Worker()
        self.__worker.readyForNextPoint.connect(self.__plotNextPoint)
        self.__worker.startThread(self.__timePoints)
        #!self.__plottingThread = self.__QThreadImplementation(self.__realTimePlotting)
        #!self.__plottingThread.start()
    def getGraph(self):
        return self.__graph