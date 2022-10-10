import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from rich.traceback import install

from constants import *

install(width=300, show_locals=True)


class WindowAdmin:
	def __init__(self, name):
		import gui # noqa


class WindowUser:
	def __init__(self, name):
		import gui # noqa


class Login(QWidget):
	def __init__(self):
		super(Login, self).__init__()
		self.resize(300, 100)

		self.user_label = QLabel('E-mail address:', self)
		self.pwd_label = QLabel('Password:', self)
		self.user_line = QLineEdit(self)
		self.user_line.setClearButtonEnabled(True)
		self.pwd_line = QLineEdit(self)
		self.pwd_line.setClearButtonEnabled(True)
		self.login_button = QPushButton('Войти', self)

		self.grid_layout = QGridLayout()
		self.h_layout = QHBoxLayout()
		self.v_layout = QVBoxLayout()

		self.lineedit_init()
		self.pushbutton_init()
		self.layout_init()

	def layout_init(self):
		self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
		self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
		self.h_layout.addWidget(self.login_button)
		self.v_layout.addLayout(self.grid_layout)
		self.v_layout.addLayout(self.h_layout)

		self.setLayout(self.v_layout)

	def lineedit_init(self):
		self.user_line.setPlaceholderText('Please enter your email')
		self.pwd_line.setPlaceholderText('Please enter your password')
		self.pwd_line.setEchoMode(QLineEdit.Password)

		self.user_line.textChanged.connect(self.check_input_func) # noqa
		self.pwd_line.textChanged.connect(self.check_input_func) # noqa

	def pushbutton_init(self):
		self.login_button.setEnabled(False)
		self.login_button.clicked.connect(self.check_login_func) # noqa

	def check_login_func(self):
		password = USER_PWD.get(self.user_line.text())
		if password != self.pwd_line.text():
			QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')
			return

		user = self.user_line.text().split('@')[0]
		if user == 'admin':
			self.windowAdmin = WindowAdmin(user) # noqa
		else:
			self.windowUser = WindowUser(user) # noqa

		self.close()

	def check_input_func(self):
		if self.user_line.text() and self.pwd_line.text():
			self.login_button.setEnabled(True)
		else:
			self.login_button.setEnabled(False)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = Login()
	w.show()
	sys.exit(app.exec_())
