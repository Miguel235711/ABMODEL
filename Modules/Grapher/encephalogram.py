#include <QPen>
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap, QPen, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from math import ceil
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from random import random


def factor(deltaX,x):
    return 1 if not x else int(ceil(x/deltaX))

def normalizedValueToBlueRedScale(x):
    # 0 is blue, 1 is red
    deltaX=1.0/1021.0
    print deltaX
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
    def __init__(self,imagePath):
        super(QWidget,self).__init__()
        image=QPixmap(imagePath)
        imageLabel=QLabel('Hello')
        imageLabel.setAlignment(Qt.AlignCenter)
        rgbValue = normalizedValueToBlueRedScale(0.8)
        imageLabel.setStyleSheet("color: rgb("+str(rgbValue[0])+","+str(rgbValue[1])+","+str(rgbValue[2])+");")
        #imageLabel.setPixmap(image.scaled(465,466))
        self.__layout=QHBoxLayout()
        self.setLayout(self.__layout)
        #self.__layout.setAlignment(Qt.AlignCenter)
        self.__layout.addWidget(imageLabel)
        #icon.setIconSize(QSize(600,600))

        with Image.open(imagePath) as im:
            draw = ImageDraw.Draw(im)
                        #x1, y1, x2, y2
            radius = 7.5
            values = []

            for i in xrange(32):
                values.append(random())

            nodes = [(190, 64), (190, 102), (178, 140), (128, 132), (148, 176), (200, 182), (171, 217), (109, 217),
                     (138, 274), (200, 256), (177, 310),(125, 327), (200, 339), (199, 369), (235, 380), (235, 298),
                     (270, 64), (270, 102), (235, 140), (287, 140), (335, 132), (318, 176), (262, 182), (235, 217),
                     (294, 217), (353, 217), (324, 274), (262, 256), (286, 310), (347, 327), (259, 339), (269, 369)]

            for coordinate in nodes:
                draw.ellipse((coordinate[0] - radius, coordinate[1] - radius, coordinate[0] + radius, coordinate[1] + radius), fill = (0,0,0))

            for i,coordinate in enumerate(nodes):
                draw.ellipse((coordinate[0] - radius, coordinate[1] - radius, coordinate[0] + radius, coordinate[1] + radius), fill = normalizedValueToBlueRedScale(values[i]))

            qim = ImageQt(im)
            pix = QtGui.QPixmap.fromImage(qim)
            imageLabel.setPixmap(pix.scaled(465,466))