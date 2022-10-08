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

with open('wpa_supplicant.conf', 'w') as f:
	ftp.retrlines(f'RETR {wpa_supplicant}', f.write)

with open('wpa_supplicant.conf') as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		if 'psk=' not in line:
			continue
		line = line[:line.index('psk=') + 4] + password
		line_num = i
		break

lines[line_num] = line

with open('wpa_supplicant.conf', 'w') as f:
	f.writelines(lines)

with open('wpa_supplicant.conf') as f:
	ftp.storlines(f'STOR {wpa_supplicant}', f)
