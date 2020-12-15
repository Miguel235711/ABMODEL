from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon



class InfoDialog:
    def __init__(self):
        self.__warningIcon=QIcon('../../Public/Images/warningIcon.png')
        self.__successIcon=QIcon('../../Public/Images/checkmarkIcon.jpg')
    def openWarningDialog(self,titulo,textoCuerpo):
        self.__showDialog(titulo,textoCuerpo,self.__warningIcon,QMessageBox.Warning)
    def openSuccessDialog(self,titulo,textoCuerpo):
        self.__showDialog(titulo,textoCuerpo,self.__successIcon,QMessageBox.Information)
    def __showDialog(self,titulo,textoCuerpo,windowIcon,icon):
        #print ('showDialog() InfoDialog')
        dialog = QMessageBox()
        dialog.setWindowTitle(titulo)
        dialog.setText(textoCuerpo)
        dialog.setStyleSheet("QLabel{font-size: 16px;}")
        dialog.setIcon(icon)
        dialog.setWindowIcon(windowIcon)
        dialog.exec_()