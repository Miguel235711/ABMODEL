from PyQt5.QtWidgets import QApplication
import file
import mainWindow
def readCV():
    cvFile=file.File('eeg_flex_007_Desconocido.csv')
    cvFile.readAndSaveData()
    return cvFile
def main():
    cvFile=readCV()
    app=QApplication([])
    mainWindowInstance=mainWindow.MainWindow('ABMODEL','images/cheese.jpg')
    #dummy=[cvFile.getAverageOfWavesAndTime(0),cvFile.getAverageOfWavesAndTime(1),cvFile.getAverageOfWavesAndTime(2),cvFile.getAverageOfWavesAndTime(3)]
    #data
    data=cvFile.getAllData()
    print(data)
    mainWindowInstance.initGraph(data)
    app.exec_()
main()