from PyQt5.QtWidgets import QWidget,QLabel,QHBoxLayout

class UserInfo(QWidget):
    labelStyleSheet="""
    QLabel{
        font: bold 15px;
    }
    """
    allInfoChildSheet="""
    border-radius:20px;
    background-color:white;
    padding: 10px;
    border-width:1.5px;
    border-color:black;
    border-style: none;
    margin-top:20px;
    margin-bottom:20px;
    """

    def __init__(self):
        super(QWidget,self).__init__()
        self.__initLayout()
    def __initLayout(self):

        #self.setStyleSheet(UserInfo.selfStyleSheet)
        self.__widget=QWidget(self)
        self.__widget.setObjectName("mainWidget")
        self.__widget.setStyleSheet(
        """
            QWidget
            {
                border-radius:20px;
                background-color:white;
                padding: 10px;
                border-width:1.5px;
                border-color:black;
                border-style: outset;
                margin-top:20px;
                margin-bottom:20px;
                width: 100%
            }
        """
        )
        horizontalLayout=QHBoxLayout()

        #fileName

        filaNameLabel=QLabel('Archivo: ')
        filaNameLabel.setStyleSheet(UserInfo.labelStyleSheet+UserInfo.allInfoChildSheet)
        horizontalLayout.addWidget(filaNameLabel)
        self.__fileName=QLabel('Registro de Torybio')
        horizontalLayout.addWidget(self.__fileName)
        self.__fileName.setStyleSheet(UserInfo.allInfoChildSheet)

        #pacientName

        pacientNameLabel=QLabel('Paciente: ')
        pacientNameLabel.setStyleSheet(UserInfo.labelStyleSheet+UserInfo.allInfoChildSheet)
        horizontalLayout.addWidget(pacientNameLabel)
        self.__pacientName=QLabel('Rodrigo')
        horizontalLayout.addWidget(self.__pacientName)
        self.__pacientName.setStyleSheet(UserInfo.allInfoChildSheet)

        #userName

        userNameLabel=QLabel('Usuario: ')
        userNameLabel.setStyleSheet(UserInfo.labelStyleSheet+UserInfo.allInfoChildSheet)
        horizontalLayout.addWidget(userNameLabel)
        self.__userName=QLabel('Torybio1302')
        horizontalLayout.addWidget(self.__userName)
        self.__userName.setStyleSheet(UserInfo.allInfoChildSheet)

        #set horizontal layout to widget

        self.__widget.setLayout(horizontalLayout)