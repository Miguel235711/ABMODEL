from PyQt5.QtWidgets import QMainWindow,QPushButton,QToolTip,QStatusBar,QLabel,QMessageBox
from PyQt5.QtGui import QFont,QIcon
import state
from threading import Thread
from time import sleep


class MainWindow(QMainWindow):

    def statusBarTester(self):
        while self.__shouldThreadsRun:
            for _ in range(400):
                if not self.__shouldThreadsRun:
                    break
                sleep(.01)
            self.__state.setConnectionState(not self.__state.getConnectionState())

    def __init__(self,title,iconPath,centralWidget):
        super(QMainWindow,self).__init__()
        self.setCentralWidget(centralWidget)
        #self.statusBar().addPermanentWidget(QLabel("Estado: "))
        #self.statusBar().addPermanentWidget(QLabel("Conectado"))
        self.__state=state.State()

        #start state tester thread

        self.__shouldThreadsRun=True
        self.__statusBarTesterThread = Thread(target=self.statusBarTester)
        self.__statusBarTesterThread.start()

        self.statusBar().addPermanentWidget(self.__state)
        
        #self.__toolBar=self.addToolBar("Main toolbar")
        #self.__toolBar.addAction(QPushButton("Menu"))

        self.__title=title
        self.__iconPath=iconPath
        self.__initUI()

    def __initUI(self):
        self.__initWindowUIMetaData()
        self.show()
        self.resize(1800,900)
        self.move(0,0)

    def __initWindowUIMetaData(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        #self.setToolTip('This is a <b>QWidget</b> widget')
        self.setWindowTitle(self.__title)
        self.setWindowIcon(QIcon(self.__iconPath))

    def closeEvent(self,event):
        
        reply = QMessageBox.question(self, 'Salir',
            "Quiere guardar los cambios?", QMessageBox.Yes | 
            QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes or reply == QMessageBox.No:
            #end all threads

            self.__shouldThreadsRun=False
            self.__statusBarTesterThread.join()

            #continue close event
            event.accept()
        else:
            event.ignore()
