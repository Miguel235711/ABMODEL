from PyQt5.QtWidgets import QApplication
import file
import mainWindow
def readCV():
    cvFile=file.File('eeg_flex_007_Desconocido.csv')
    cvFile.readAndSaveData()
def main():
    readCV()
    app=QApplication([])
    mainWindowInstance=mainWindow.MainWindow('ABMODEL','images/cheese.jpg')
    app.exec_()
main()