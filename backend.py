from string import ascii_letters, digits, punctuation
from typing import Final
from random import choice, randint

PASSWORD_LENGTH: Final = randint(10, 16)

printable = digits + ascii_letters + punctuation

password = ''
for x in range(PASSWORD_LENGTH):
    password += choice(printable)

print(password)
