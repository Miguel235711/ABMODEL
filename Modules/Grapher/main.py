import sys
from PyQt5.QtWidgets import QApplication
sys.path.append('../Data/Reader')
import file
import container
import mainWindow
def readCV():
    cvFile=file.File('../../Data/Graph/eeg_flex_007_Desconocido.csv')
    cvFile.readAndSaveData()
    return cvFile
def main():
    cvFile=readCV()
    app=QApplication([])
    containerInstance=container.Container(app)
    #dummy=[cvFile.getAverageOfWavesAndTime(0),cvFile.getAverageOfWavesAndTime(1),cvFile.getAverageOfWavesAndTime(2),cvFile.getAverageOfWavesAndTime(3)]
    #data
    mainWindowInstance=mainWindow.MainWindow('ABMODEL','../../Public/Images/cheese.jpg',containerInstance)
    data=cvFile.getAllData()
    #print(data)
    containerInstance.initGraphs(data)
    sys.exit(app.exec_())
main()