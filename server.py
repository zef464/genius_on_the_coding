# coding=utf-8
# Изменить пароль окна
# client.py

import socket

server = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
server.bind(('192.168.11.1', 22))  # Привязать IP / порт
server.listen(5)  # прослушивание
print('starting....')
conn, addr = server.accept()  # Подключить
print(conn)
print('client addr', addr)
print('ready to recv the passwd...')
client_msg = conn.recv(1024)
print('client passwd changed: %s' % client_msg)
conn.send(client_msg.upper())
conn.close()
server.close()