from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout,QMessageBox,QToolTip,QLabel,QSizePolicy,QDialog,QLineEdit,QFileDialog

class MultiGraphContainer(QWidget):
    __waveColors=[(115,124,161),(203,203,44),(199,28,28),(195,195,195)]
    def __init__(self):
        super(QWidget,self).__init__()
        