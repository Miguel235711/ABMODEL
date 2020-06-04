# coding=utf-8
from PyQt5.QtWidgets import QApplication
import mainWindow
import menuMain as regs

def main():
    app=QApplication([])
    regsInstance= regs.Pantalla()
    #dummy=[cvFile.getAverageOfWavesAndTime(0),cvFile.getAverageOfWavesAndTime(1),cvFile.getAverageOfWavesAndTime(2),cvFile.getAverageOfWavesAndTime(3)]
    #data
    mainWindowInstance=mainWindow.MainWindow('ABMODEL','../../Public/Images/cheese.jpg',regsInstance)
    #print(data)

    app.exec_()
main()