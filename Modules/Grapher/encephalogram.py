#include <QPen>
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap, QPen, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from math import ceil
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from  threadWorker import Worker
#from random import random


def factor(deltaX,x):
    return 1 if not x else int(ceil(x/deltaX))

def normalizedValueToBlueRedScale(x):
    # 0 is blue, 1 is red
    deltaX=1.0/1021.0
    #print deltaX
    if x<=deltaX * 256:
        return (0,factor(deltaX,x)-1,255)
    x -= deltaX * 256
    if x<=deltaX * 255:
        return (0,255,255-factor(deltaX,x))
    x -= deltaX * 255
    if x<=deltaX * 255:
        return (factor(deltaX,x),255,0)
    x -= deltaX * 255
    return (255,255-factor(deltaX,x),0)

class Encephalogram(QWidget):
    __radius = 7.5
    __nodes = [
        (190, 64), (190, 102), (178, 140), (128, 132), (148, 176), (200, 182), (171, 217), (109, 217),
        (138, 274), (200, 256), (177, 310),(125, 327), (200, 339), (199, 369), (235, 380), (235, 298),
        (270, 64), (270, 102), (235, 140), (287, 140), (335, 132), (318, 176), (262, 182), (235, 217),
        (294, 217), (353, 217), (324, 274), (262, 256), (286, 310), (347, 327), (259, 339), (269, 369)
    ]

    def __updateImage(self):
        self.__imageLabel.setPixmap(QtGui.QPixmap.fromImage(ImageQt(self.__im)).scaled(465,466))

    def __init__(self,imagePath,app):
        #data =[(time0,[val0,val1,...,val31]),(time1,[val0,val1,...,val31]),...]
        super(QWidget,self).__init__()
        #imageLabel.setAlignment(Qt.AlignCenter)
        #rgbValue = normalizedValueToBlueRedScale(0.8)
        #imageLabel.setStyleSheet("color: rgb("+str(rgbValue[0])+","+str(rgbValue[1])+","+str(rgbValue[2])+");")
        #imageLabel.setPixmap(image.scaled(465,466))
        self.__app=app
        self.__layout=QHBoxLayout()
        self.setLayout(self.__layout)
        self.__i=0
        #self.__layout.setAlignment(Qt.AlignCenter)
        #icon.setIconSize(QSize(600,600))
        with Image.open(imagePath) as self.__im:
            self.__draw = ImageDraw.Draw(self.__im)
                        #x1, y1, x2, y2
            #values = []

            #for i in xrange(32):
            #    values.append(random())
            for coordinate in self.__nodes:
                self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = (0,0,0))
            self.__imageLabel=QLabel()
            self.__layout.addWidget(self.__imageLabel)
            self.__updateImage()
    @QtCore.pyqtSlot()
    def setPause(self,pause):
        self.__worker.setPause(pause)
    def getPause(self):
        return self.__worker.getPause()
    def __plotNext(self):
        #print '__plotNext'
        #print 'current values length:',self.__values[self.__i]
        print 'self.__i',self.__i,'len(self.__values)',len(self.__values)
        if self.__i < len(self.__values):
            for i,coordinate in enumerate(self.__nodes):
                self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = normalizedValueToBlueRedScale(self.__values[self.__i][i]))
            self.__i+=1
        else:
            #no data, display zero
             for coordinate in self.__nodes:
                self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = normalizedValueToBlueRedScale(0))
        self.__updateImage()
    def __saveData(self,data):
        self.__times= [ data[moment][0] for moment in xrange(len(data)) ]
        self.__values = [ data[moment][1] for moment in xrange(len(data))]
    def initEncephalogram(self,data):
        print 'initEncephalogram'
        self.__saveData(data)
        self.__worker = Worker()
        self.__worker.readyForNextPoint.connect(self.__plotNext)
        #print self.__times
        self.__worker.startThread(self.__times,self.__app)
        #self.setPause(not self.getPause())