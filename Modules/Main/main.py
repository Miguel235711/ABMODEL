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

class MainWindow(QMainWindow):
    def __init__(self,title,iconPath,centralWidget):
        super(QMainWindow,self).__init__()
        self.__title=title
        self.__iconPath=iconPath
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
        self.show()
        self.showFullScreen()
        # self.resize(1920,1080)
        self.move(0,0)
    def initWindowUIMetaData(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setWindowTitle(self.__title)
        self.setWindowIcon(QIcon(self.__iconPath))
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Salir',
            "Quiere guardar los cambios?", QMessageBox.Yes | 
            QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes or reply == QMessageBox.No:
            #continue close event
            event.accept()
        else:
            event.ignore()
centralWidget,mainWindow=None,None
def changeToRegister():
    global centralWidget,mainWindow
    centralWidget=registrationMain.Pantalla(changeToMenu)
    mainWindow.setCentralWidget(centralWidget)
def changeToLogIn():
    global centralWidget,mainWindow
    centralWidget=LogInMain.Pantalla(changeToMenu,changeToUserMenu)
    mainWindow.setCentralWidget(centralWidget)
def changeToMenu():
    global centralWidget,mainWindow
    centralWidget=menuMain.Pantalla(changeToLogIn,changeToRegister)
    mainWindow.setCentralWidget(centralWidget)
def changeToUserMenu(username):
    global centralWidget,mainWindow
    centralWidget=userMenu.Pantalla(changeToMenu,username)
    mainWindow.setCentralWidget(centralWidget)
def main():
    global centralWidget,mainWindow
    app=QApplication([])
    centralWidget=menuMain.Pantalla(changeToLogIn,changeToRegister)
    mainWindow=MainWindow('ABMODEL','../../Public/Images/cheese.jpg',centralWidget)
    #dummy=[cvFile.getAverageOfWavesAndTime(0),cvFile.getAverageOfWavesAndTime(1),cvFile.getAverageOfWavesAndTime(2),cvFile.getAverageOfWavesAndTime(3)]
    #data
    #print(data)
    app.exec_()
main()