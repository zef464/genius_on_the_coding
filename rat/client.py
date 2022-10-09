import socket
from time import sleep

from constants import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa
s.connect((host, rat_port))
s.bind((host, rat_port))
s.listen()

print("[*] Waiting for the server...")
client, addr = s.accept()

new_password = client.recv(MAX_PASSWORD_BYTES)
print(f"[*] Connection is established successfully")
print(new_password)

s.close()
