# encoding: utf-8
from PyQt5.QtCore import QObject,pyqtSignal
from threading import Thread
from time import sleep

import sys
sys.path.append('../GlobalInstances')
from globalInstances import GlobalInstances

class Worker(QObject):
    readyForNextPoint = pyqtSignal()
    def __init__(self):
        #print 'Worker __init__'
        super(QObject,self).__init__()
        self.__continue=True
        self.__pause=True
    def __changeFlagToFalse(self):
        self.__continue=False
    def startThread(self,timePoints):
        #print 'start thread'
        #print 'inside Function()'
        self.__timePoints=timePoints
        self.__thread=Thread(target=self.__func)
        GlobalInstances.getApp().aboutToQuit.connect(self.__changeFlagToFalse)
        self.__thread.start()
    def __func(self):
        #print 'Worker __func()'
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
        #continue if not more data, every 0.250 s
        while True:
            while(self.__pause):
                if not self.__continue:
                    return
                sleep(1)
            if not self.__continue:
                return
            sleep(0.250)
            self.readyForNextPoint.emit()
    def setPause(self,pause):
        self.__pause=pause
    def getPause(self):
        return self.__pause