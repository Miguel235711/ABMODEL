from PyQt5.QtWidgets import QMainWindow,QPushButton,QToolTip,QStatusBar,QLabel,QMessageBox
from PyQt5.QtGui import QFont,QIcon
import state

class MainWindow(QMainWindow):
    def __init__(self,title,iconPath,centralWidget):
        super(QMainWindow,self).__init__()
        self.setCentralWidget(centralWidget)
        #self.statusBar().addPermanentWidget(QLabel("Estado: "))
        #self.statusBar().addPermanentWidget(QLabel("Conectado"))
        self.statusBar().addPermanentWidget(state.State())
        self.title=title
        self.iconPath=iconPath
        self.initUI()

    def initUI(self):
        self.initWindowUIMetaData()
        self.show()
        self.resize(1800,900)
        self.move(0,0)

    def initWindowUIMetaData(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconPath))
    def closeEvent(self,event):
        
        reply = QMessageBox.question(self, 'Salir',
            "Quiere guardar los cambios?", QMessageBox.Yes | 
            QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes or reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()
