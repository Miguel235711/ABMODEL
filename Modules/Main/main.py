# encoding: utf-8
from PyQt5.QtWidgets import QMainWindow,QPushButton,QToolTip,QStatusBar,QLabel,QMessageBox,QApplication
from PyQt5.QtGui import QFont,QIcon
import sys
from PyQt5.QtCore import Qt
sys.path.append('../Menu')
import menuMain
sys.path.append('../Registration')
import registrationMain
sys.path.append('../Log-In')
import LogInMain
sys.path.append('../UserMenu')
import userMenu
sys.path.append('../Grapher')
import state
import container
sys.path.append('../Data/Reader')
import file
sys.path.append('../GlobalInstances')
import globalInstances

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
        self.__title=title
        self.__iconPath=iconPath
        self.setBackground()
        self.setCentralWidget(centralWidget)
        self.initUI()
        #self.setBackground()
    def setBackground(self):
        self.setStyleSheet(
        """
        QMainWindow{
            background-image:url(../../Public/Images/background.png)
        }
        """)
    def initUI(self):
        self.initWindowUIMetaData()
        #self.show()
        self.showFullScreen()
        # self.resize(1920,1080)
        #self.move(0,0)
    def initWindowUIMetaData(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle(self.__title)
        self.setWindowIcon(QIcon(self.__iconPath))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
    def stopBarThreads(self):
        self.__shouldThreadsRun=False
        self.__statusBarTesterThread.join()
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Salir',
            u'¿Quiere guardar los cambios?', QMessageBox.Yes | 
            QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes or reply == QMessageBox.No:
            #end running threads
            self.stopBarThreads()

            #continue close event
            event.accept()
        else:
            event.ignore()
    def setElseAsCentralWidget(self,widget):
        #remove grapher related things
        try:   
            self.stopBarThreads()
            self.statusBar().removeWidget(self.__state)
            self.statusBar().setStyleSheet(
            """
                background-color:none;
            """
            )
        except:
            print('statusBar not defined yet')
        #set as central widget
        self.setCentralWidget(widget)
    def setGrapherAsCentralWidget(self,widget):
        self.__state=state.State()
        #start state tester thread

        self.__shouldThreadsRun=True
        self.__statusBarTesterThread = Thread(target=self.statusBarTester)
        self.__statusBarTesterThread.start()

        self.statusBar().addPermanentWidget(self.__state)
        self.statusBar().setStyleSheet(
        """
        background-color:white;
        """
        )
        self.statusBar().setFixedHeight(40)
        self.setCentralWidget(widget)
def readCV(path):
    cvFile=file.File(path)
    cvFile.readAndSaveData()
    return cvFile
mainWindow,app=None,None
def endApp():
    global mainWindow
    mainWindow.close()
def changeToRegister():
    global mainWindow
    mainWindow.setElseAsCentralWidget(registrationMain.Pantalla(changeToMenu))
def changeToLogIn():
    global mainWindow
    mainWindow.setElseAsCentralWidget(LogInMain.Pantalla(changeToMenu,changeToUserMenu))
def changeToMenu():
    global mainWindow
    mainWindow.setElseAsCentralWidget(menuMain.Pantalla(changeToLogIn,changeToRegister,endApp))
def changeToUserMenu(username):
    global mainWindow
    mainWindow.setElseAsCentralWidget(userMenu.Pantalla(changeToMenu,changeToGrapher,username))
def changeToGrapher(username,filePath):
    global mainWindow
    cvFile=readCV(filePath)
    graphData=cvFile.getAverageData()
    encephalogramData=cvFile.getNormalizedNodeData()
    containerInstance=container.Container(changeToUserMenu,username,filePath)
    containerInstance.initGraphsAndEncephalograms(graphData,encephalogramData)
    mainWindow.setGrapherAsCentralWidget(containerInstance)
    #print(data)
def main():
    global mainWindow,app
    app=QApplication([])
    globalInstances.GlobalInstances.buildInstances(app)
    mainWindow=MainWindow('ABMODEL','../../Public/Images/cheese.jpg',menuMain.Pantalla(changeToLogIn,changeToRegister,endApp))
    #changeToGrapher()
    #dummy=[cvFile.getAverageOfWavesAndTime(0),cvFile.getAverageOfWavesAndTime(1),cvFile.getAverageOfWavesAndTime(2),cvFile.getAverageOfWavesAndTime(3)]
    #data
    #print(data)
    sys.exit(app.exec_())
main()