#include <QPen>
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap, QPen, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt,QPoint
from math import ceil
from PIL import Image, ImageDraw,ImageFont
from PIL.ImageQt import ImageQt
from  threadWorker import Worker
from datetime import timedelta
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
    #__nodes32Copy = [
    #    (190, 64), (190, 102), (178, 140), (128, 132), (148, 176), (200, 182), (171, 217), (109, 217),
    #    (138, 274), (200, 256), (177, 310),(125, 327), (200, 339), (199, 369), #(235, 380), (235, 298),
    #    (270, 64), (270, 102), (235, 140), (287, 140), (335, 132), (318, 176), (262, 182), (235, 217),
    #    (294, 217), (353, 217), (324, 274), (262, 256), (286, 310), (347, 327), (259, 339), (269, 369)
    #]
    __nodes32 = [
        (190, 64,'Fp1'), (190, 102,'AF3'), (178, 140,'F3'), (128, 132,'F7'), (148, 176,'FC5'), (200, 182,'FC1'), (171, 217,'C3'), (109, 217,'T7'),
        (138, 274,'CP5'), (200, 256,'CP1'), (177, 310,'P3'),(125, 327,'P7'), (200, 339,'PO3'), (199, 369,'O1'), (235, 380,'Oz'), (235, 298,'Pz'),
        (270, 64,'Fp2'), (270, 102,'AF4'), (235, 140,'Fz'), (287, 140,'F4'), (335, 132,'F8'), (318, 176,'FC6'), (262, 182,'FC2'), (235, 217,'Cz'),
        (294, 217,'C4'), (353, 217,'T8'), (324, 274,'CP6'), (262, 256,'CP2'), (286, 310,'P4'), (347, 327,'P8'), (259, 339,'PO4'), (269, 369,'O2'),
    ]
    __nodes14 = [
        (190, 64,'AF3'), (128, 132,'F7'), (190, 102,'F3'), (178,140,'FC5'), (109, 217,'T7'), (177, 310,'P7'), (199, 369,'O1'), 
        (269, 369,'O2'), (286, 310,'P8'), (353, 217,'T8'), (287, 140,'FC6'), (270, 102,'F4'), (335, 132,'F8'), (270, 64,'AF4') 
    ]
    __nodes5 = [
        (190, 102,'AF3'), (109, 217,'T7'), (235, 298,'Pz'), (353, 217,'T8'), (270, 102,'AF4'), 
    ]
    __timePrefixLabel='Tiempo: '
    def __updateImage(self):
        self.__imageLabel.setPixmap(QtGui.QPixmap.fromImage(ImageQt(self.__im)).scaled(465,466))

    def __init__(self,imagePath,name,color):
        #data =[(time0,[val0,val1,...,val31]),(time1,[val0,val1,...,val31]),...]
        super(QWidget,self).__init__()
        #imageLabel.setAlignment(Qt.AlignCenter)
        #rgbValue = normalizedValueToBlueRedScale(0.8)
        #imageLabel.setStyleSheet("color: rgb("+str(rgbValue[0])+","+str(rgbValue[1])+","+str(rgbValue[2])+");")
        #imageLabel.setPixmap(image.scaled(465,466))
        self.__mainLayout=QVBoxLayout()
        self.__encephalogramLayout=QHBoxLayout()
        self.__titleLayout=QHBoxLayout()
        self.__currentTime=0
        label=QLabel(name)
        label.setFixedSize(200,100)
        label.setAlignment(Qt.AlignCenter)
        backgroundColor="background:rgb"+"("+str(color[0])+","+str(color[1])+","+str(color[2])+");"
        #print backgroundColor
        label.setStyleSheet("""
            color:black;
            font: bold 50px;"""+
            backgroundColor)
        self.__mainLayout.addWidget(label,alignment=Qt.AlignHCenter)
        self.__mainLayout.addLayout(self.__encephalogramLayout)
        self.__timeLabel=QLabel('Tiempo: 0:00:00.00')
        self.__timeLabel.setStyleSheet("""
            color:black;
            font: bold 30px;
        """)
        self.__timeLabel.setAlignment(Qt.AlignCenter)
        self.__mainLayout.addWidget(self.__timeLabel,alignment=Qt.AlignHCenter)
        self.setLayout(self.__mainLayout)
        self.__mainLayout.setAlignment(Qt.AlignCenter)
        self.__i=0
        #self.__layout.setAlignment(Qt.AlignCenter)
        #icon.setIconSize(QSize(600,600))
        with Image.open(imagePath) as self.__im:
            self.__draw = ImageDraw.Draw(self.__im)
                        #x1, y1, x2, y2
            #values = []

            #for i in xrange(32):
            #    values.append(random())
            #for coordinate in self.__nodes32:
                #self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = (0,0,0))
            self.__imageLabel=QLabel()
            self.__encephalogramLayout.addWidget(self.__imageLabel)
            scale=QLabel()
            scale.setPixmap(QPixmap('../../Public/Images/encephalogramScaleIcon.png').scaled(100,500))
            self.__encephalogramLayout.addWidget(scale)
            self.__updateImage()
    @QtCore.pyqtSlot()
    def setPause(self,pause):
        self.__worker.setPause(pause)
    def getPause(self):
        return self.__worker.getPause()
    def __updateTimeLabel(self):
        #self.__timeLabel.setText((self.__timePrefixLabel+"{:.2f}").format(timedelta(seconds=self.__currentTime).total_seconds()))
        timeLabel=str(timedelta(seconds=self.__currentTime))
        pointIndex = timeLabel.find('.')
        timeLabel=timeLabel[0:pointIndex+3]
        self.__timeLabel.setText(self.__timePrefixLabel+timeLabel)
    def __plotNext(self):
        #print '__plotNext'
        #print 'current values length:',self.__values[self.__i]
        #print 'self.__i',self.__i,'len(self.__values)',len(self.__values)
        print('len of self.__values: {}'.format(len(self.__values[0])))
        if self.__i < len(self.__values):
            #print('nodes32 len{}'.format(len(chosenNodes)))
            for i,coordinate in enumerate(self.__chosenNodes):
                #print('i = {}, len(self.__values[self.__i)) = {}'.format(i,len(self.__values[self.__i])))
                self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = normalizedValueToBlueRedScale(self.__values[self.__i][i]))
            self.__currentTime=self.__times[self.__i]
            #print 'time:',self.__currentTime
            self.__updateTimeLabel()
            self.__i+=1
        else:
            #no data, display zero
            for coordinate in self.__chosenNodes:
                self.__draw.ellipse((coordinate[0] - self.__radius, coordinate[1] - self.__radius, coordinate[0] + self.__radius, coordinate[1] + self.__radius), fill = normalizedValueToBlueRedScale(0))
            self.__currentTime+=0.250
            self.__updateTimeLabel()
        self.__updateImage()
    def __saveData(self,data):
        self.__times= [ data[moment][0] for moment in range(len(data)) ]
        self.__values = [ data[moment][1] for moment in range(len(data))]
        numberOfNodes = len(self.__values[0])
        print('numberOfNodes {}'.format(numberOfNodes))
        self.__chosenNodes = self.__nodes32 if numberOfNodes  == 32 else (self.__nodes14 if numberOfNodes == 14 else (self.__nodes5 if numberOfNodes == 5 else None))
        #set node labels
        for coordinate in self.__chosenNodes:
            self.__draw.text((coordinate[0] + self.__radius, coordinate[1] + self.__radius),coordinate[2],font = ImageFont.truetype("fonts/arial.ttf",size=13))
    def initEncephalogram(self,data):
        #print 'initEncephalogram'
        self.__saveData(data)
        self.__worker = Worker()
        self.__worker.readyForNextPoint.connect(self.__plotNext)
        #print self.__times
        self.__worker.startThread(self.__times)
        #self.setPause(not self.getPause())
    #def mouseMoveEvent(self,event):
    #    print('mouseMoveEvent pos: {}'.format(event.pos()))
    #    showText(QPoint(0,0),"hello")