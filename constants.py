from random import randint
from string import ascii_letters, digits, punctuation
# from typing import Final

PASSWORD_LENGTH = randint(10, 16)

printable = digits + ascii_letters + punctuation

host = '192.168.11.1'

ftp_username = 'pi'
ftp_password = 'butpass1014'
ftp_port = 21

rat_port = 10_000
MAX_PASSWORD_BYTES = 60

# wpa_supplicant = '/etc/wpa_supplicant/wpa_supplicant.conf'
wpa_supplicant = '../wpa_supplicant.conf'
