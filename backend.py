from random import choice
from ftplib import FTP
from constants import *

new_password = ''
for x in range(PASSWORD_LENGTH):
    new_password += choice(printable)

# -----------------

ftp = FTP(source_address=(host, ftp_port))  # connect to host, default port
message = ftp.login(user=username, passwd=password)

assert message == FTP_SUCCESS_LOGIN

with open('wpa_supplicant.conf', 'wb') as f:
    ftp.retrbinary(f'RETR {wpa_supplicant}', f.write)

