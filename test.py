# import random
# pas = ''
# for x in range(10):
#     pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
# print(pas)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.resize(400, 400)
        self.WidgetsWin = QtWidgets.QWidget(Win)
        self.WidgetsWin.setObjectName("WidgetsWin")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.WidgetsWin)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.WidgetsWin)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 376))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbnt = QtWidgets.QRadioButton(self.frame_2)
        self.rbnt.setObjectName("rbnt")
        self.verticalLayout_2.addWidget(self.rbnt)
        self.rbnt_2 = QtWidgets.QRadioButton(self.frame_2)
        self.rbnt_2.setObjectName("rbnt_2")
        self.verticalLayout_2.addWidget(self.rbnt_2)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbnt_3 = QtWidgets.QRadioButton(self.frame)
        self.rbnt_3.setObjectName("rbnt_3")
        self.verticalLayout.addWidget(self.rbnt_3)
        # self.rbnt_4 = QtWidgets.QRadioButton(self.frame)
        # self.rbnt_4.setObjectName("rbnt_4")
        # self.verticalLayout.addWidget(self.rbnt_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        Win.setCentralWidget(self.WidgetsWin)

        self.retranslateUi(Win)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "MainWindow"))
        self.rbnt.setText(_translate("Win", "rbnt 1"))
        self.rbnt_2.setText(_translate("Win", "rbnt 2"))
        self.rbnt_3.setText(_translate("Win", "rbnt 3"))
        # self.rbnt_4.setText(_translate("Win", "rbnt 4"))


class MainWindow(QtWidgets.QMainWindow, Ui_Win):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window1 = MainWindow()
    Window1.show()
    sys.exit(app.exec_())