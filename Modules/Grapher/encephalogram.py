from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize

class Encephalogram(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        image=QPixmap('../../Public/Images/electroEncephalogram1Icon.png')
        imageLabel=QLabel()
        imageLabel.setPixmap(image.scaled(1500,600))
        self.__layout=QVBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.addWidget(imageLabel)
        #icon.setIconSize(QSize(600,600))