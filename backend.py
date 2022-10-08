from random import choice
import pysftp
from constants import *

new_password = ''
for x in range(PASSWORD_LENGTH):
	new_password += choice(printable)

# -----------------
print(new_password)

sftp = pysftp.Connection(host, username=username, password=password, port=ftp_port)
print('step 0 ready')

sftp.get(wpa_supplicant)
print('step 1 ready')

with open('wpa_supplicant.conf') as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		if 'psk=' not in line:
			continue
		line = line[:line.index('psk=') + 4] + password
		line_num = i
		break
print('step 2 ready')

lines[line_num] = line

with open('wpa_supplicant.conf', 'w') as f:
	f.writelines(lines)
print('step 3 ready')

sftp.put(wpa_supplicant)
print('step 4 ready')

sftp.close()
