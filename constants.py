from random import randint
from string import ascii_letters, digits, punctuation
from typing import Final

PASSWORD_LENGTH: Final = randint(10, 16)

printable = digits + ascii_letters + punctuation

host: Final[str] = '192.168.11.1'
username: Final[str] = 'pi'
password: Final[str] = 'butpass1014'
ftp_port: Final[int] = 22

FTP_SUCCESS_LOGIN: Final[str] = '230 Login successful.'

wpa_supplicant: Final[str] = '/etc/wpa_supplicant/wpa_supplicant.conf'