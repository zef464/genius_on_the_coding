from random import choice
from constants import *

new_password = ''
for x in range(PASSWORD_LENGTH):
	new_password += choice(printable)

print(new_password)
# -----------------

with open(wpa_supplicant) as f:
	lines = f.readlines()
	for i, line in enumerate(lines):
		if 'psk=' not in line:
			continue
		line = line[:line.index('psk=') + 4] + password
		line_num = i
		break
print('step 1 ready')

lines[line_num] = line

with open('wpa_supplicant.conf', 'w') as f:
	f.writelines(lines)
print('step 2 ready')
