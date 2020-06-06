from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize
from math import ceil

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
        rgbValue = normalizedValueToBlueRedScale(0.8)
        imageLabel.setStyleSheet("color: rgb("+str(rgbValue[0])+","+str(rgbValue[1])+","+str(rgbValue[2])+");")
        #imageLabel.setPixmap(image.scaled(1500,800))
        self.__layout=QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.addWidget(imageLabel)
        #icon.setIconSize(QSize(600,600))