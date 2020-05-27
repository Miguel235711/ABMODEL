from PyQt5.QtWidgets import QWidget
from pyqtgraph import PlotWidget,mkPen,setConfigOption

class Graph():
    def __init__(self,timePoints,wavePoints,waveColor):
        setConfigOption('background',(230,230,230))
        setConfigOption('foreground',(0,0,0))
        self.__graph=PlotWidget()
        self.__timePoints=timePoints
        self.__wavePoints=wavePoints
        self.__waveColor=waveColor
        ##times=[pair[0] for pair in data ]
        ##firstWave=[pair[1][0] for pair in data]
        ##self.graphWidget.plot(times,firstWave)
    def plotGraph(self):
        self.__graph.plot(self.__timePoints,self.__wavePoints,pen=mkPen(color=self.__waveColor,width=3))
    def getGraph(self):
        return self.__graph