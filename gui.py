import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from rich.traceback import install
from constants import *
from rat.client import change_password

install(width=300, show_locals=True)


class Ui_Dialog(object):  # noqa
	def __init__(self, Dialog):  # noqa
		Dialog.setObjectName("Dialog")
		Dialog.resize(573, 300)
		Dialog.setStyleSheet("background-color: rgb(0, 0, 0)")
		font = QtGui.QFont()
		font.setFamily("Niagara Solid")

		self.line = QtWidgets.QFrame(Dialog)  # noqa
		self.line.setGeometry(QtCore.QRect(270, -20, 16, 321))
		self.line.setMinimumSize(QtCore.QSize(0, 0))
		self.line.setSizeIncrement(QtCore.QSize(90, 90))
		self.line.setBaseSize(QtCore.QSize(90, 90))

		self.line.setFont(font)
		self.line.setMouseTracking(False)
		self.line.setTabletTracking(False)
		self.line.setAcceptDrops(False)
		self.line.setAutoFillBackground(False)
		self.line.setMidLineWidth(5)
		self.line.setFrameShape(QtWidgets.QFrame.VLine)  # noqa
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)  # noqa
		self.line.setObjectName("line")

		self.line_2 = QtWidgets.QFrame(Dialog)  # noqa
		self.line_2.setGeometry(QtCore.QRect(-10, 150, 281, 20))
		self.line_2.setMidLineWidth(5)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)  # noqa
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)  # noqa
		self.line_2.setObjectName("line_2")

		self.textBrowsers = []  # noqa

		for i, coord in enumerate(textBrowsers_coords):
			tmp = QtWidgets.QTextBrowser(Dialog)
			tmp.setGeometry(QtCore.QRect(*coord))
			tmp.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 255, 255);")
			tmp.setObjectName(f"textBrowser_{i}")
			self.textBrowsers.append(tmp)

		for i, coord in enumerate(lineEdit_coords):
			tmp = QtWidgets.QLineEdit(Dialog)
			tmp.setGeometry(QtCore.QRect(*coord))
			tmp.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 255, 255);")
			tmp.setText('')
			tmp.setObjectName(f"lineEdit_{i}")

		for i, coord in enumerate(checkBox_coords):
			tmp = QtWidgets.QCheckBox(Dialog)
			tmp.setGeometry(QtCore.QRect(*coord))
			tmp.setStyleSheet("background-color: rgb(0, 0, 0);\n color: rgb(255, 255, 255);")
			tmp.setText("")
			tmp.setObjectName(f"checkBox_{i}")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog): # noqa
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Program"))

		for i, tmp in enumerate(self.textBrowsers):
			if i == 5:
				tmp.setHtml(_translate("Dialog", htmls[i] % 'loading...'))
				new_password = change_password()
				tmp.setHtml(_translate("Dialog", htmls[i] % new_password))
			else:
				tmp.setHtml(_translate("Dialog", htmls[i] % (textBrowsers_values[i])))


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog(Dialog)
Dialog.show()
app.exec_()
