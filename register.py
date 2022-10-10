from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout
from constants import *


class RegisterPage(QDialog):
	def __init__(self):
		super(SigninPage, self).__init__()
		self.signin_user_label = QLabel('E-mail:')
		self.signin_pwd_label = QLabel('Password:')
		self.signin_pwd2_label = QLabel('Password:')
		self.signin_user_line = QLineEdit()
		self.signin_pwd_line = QLineEdit()
		self.signin_pwd2_line = QLineEdit()
		self.signin_button = QPushButton('Sign in')

		self.user_h_layout = QHBoxLayout()
		self.pwd_h_layout = QHBoxLayout()
		self.pwd2_h_layout = QHBoxLayout()
		self.all_v_layout = QVBoxLayout()

		self.lineedit_init()
		self.pushbutton_init()
		self.layout_init()

	def layout_init(self):
		self.user_h_layout.addWidget(self.signin_user_label)
		self.user_h_layout.addWidget(self.signin_user_line)
		self.pwd_h_layout.addWidget(self.signin_pwd_label)
		self.pwd_h_layout.addWidget(self.signin_pwd_line)
		self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
		self.pwd2_h_layout.addWidget(self.signin_pwd2_line)

		self.all_v_layout.addLayout(self.user_h_layout)
		self.all_v_layout.addLayout(self.pwd_h_layout)
		self.all_v_layout.addLayout(self.pwd2_h_layout)
		self.all_v_layout.addWidget(self.signin_button)

		self.setLayout(self.all_v_layout)

	def lineedit_init(self):
		self.signin_pwd_line.setEchoMode(QLineEdit.Password)
		self.signin_pwd2_line.setEchoMode(QLineEdit.Password)

		self.signin_user_line.textChanged.connect(self.check_input_func) # noqa
		self.signin_pwd_line.textChanged.connect(self.check_input_func) # noqa
		self.signin_pwd2_line.textChanged.connect(self.check_input_func) # noqa

	def pushbutton_init(self):
		self.signin_button.setEnabled(False)
		self.signin_button.clicked.connect(self.check_signin_func) # noqa

	def check_input_func(self):
		if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
			self.signin_button.setEnabled(True)
		else:
			self.signin_button.setEnabled(False)


def check_signin_func(self):
	if self.signin_pwd_line.text() != self.signin_pwd2_line.text():
		QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not Same!')
	elif self.signin_user_line.text() not in USER_PWD:
		USER_PWD[self.signin_user_line.text()] = self.signin_pwd_line.text()
		QMessageBox.information(self, 'Information', 'Register Successfully')
		self.close()
	else:
		QMessageBox.critical(self, 'Wrong', 'This Username Has Been Registered!')

	self.signin_user_line.clear()
	self.signin_pwd_line.clear()
	self.signin_pwd2_line.clear()
