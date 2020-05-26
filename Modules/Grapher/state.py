from PyQt5.QtWidgets import QWidget,QToolTip,QStatusBar,QLabel,QMessageBox,QHBoxLayout
from PyQt5.QtGui import QFont,QIcon,QPixmap

class State(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.container=QHBoxLayout()
        self.container.addWidget(QLabel("Estado: "))
        self.connectionLabel=QLabel("Conectado")
        self.connectionLabel.setStyleSheet("color: green")
        self.container.addWidget(self.connectionLabel)
        connectionQPixmap=QPixmap("../../Public/Images/connectedIcon.png")
        connectionQPixmap = connectionQPixmap.scaledToWidth(30)
        self.connectionImage=QLabel()
        self.connectionImage.setPixmap(connectionQPixmap)
        self.container.addWidget(self.connectionImage)
        self.setLayout(self.container)
