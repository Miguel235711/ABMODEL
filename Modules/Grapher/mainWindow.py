from PyQt5.QtWidgets import QWidget,QMainWindow, QPushButton, QVBoxLayout,QMessageBox,QToolTip
from PyQt5.QtGui import QIcon,QFont
from pyqtgraph import PlotWidget, plot

class MainWindow(QMainWindow):
    def __init__(self,title,iconPath):
        super(QWidget,self).__init__()
        self.title=title
        self.iconPath=iconPath
        self.initUI()
    def initGraph(self,data):
        #data is [(T1,[A,B,C,D]),(T2,[E,F,G,H]),...]
        self.graphWidget=PlotWidget()
        self.setCentralWidget(self.graphWidget)
        #hour = [1,2,3,4,5,6,7,8,9,10]
        #temperature = [30,32,34,32,33,31,29,32,35,45]
        times=[pair[0] for pair in data ]
        firstWave=[pair[1][0] for pair in data]
        self.graphWidget.plot(times,firstWave)
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconPath))
        self.showMaximized()
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()