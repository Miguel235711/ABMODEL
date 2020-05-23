from PyQt5.QtWidgets import QWidget
from pyqtgraph import PlotWidget,mkPen,setConfigOption

class Graph():
    def __init__(self,timePoints,wavePoints,waveColor):
        setConfigOption('background',(230,230,230))
        setConfigOption('foreground',(0,0,0))
        self.graph=PlotWidget()
        self.timePoints=timePoints
        self.wavePoints=wavePoints
        self.waveColor=waveColor
        ##times=[pair[0] for pair in data ]
        ##firstWave=[pair[1][0] for pair in data]
        ##self.graphWidget.plot(times,firstWave)
    def plotGraph(self):
        self.graph.plot(self.timePoints,self.wavePoints,pen=mkPen(color=self.waveColor,width=3))
    def getGraph(self):
        return self.graph