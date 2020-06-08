from PyQt5.QtWidgets import QWidget,QSizePolicy

def getDummyWidget():
    dummy = QWidget()
    dummy.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
    return dummy