import string
import random
import subprocess
from subprocess import CompletedProcess
from typing import Any

# Printing The Logo

logo = """"
     \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
    \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m    ___  _  _                                _
   \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[34m-\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m  | _ \| || | ___ ___ _ __ __  ___  _ _  __| |
   \u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m  |  _/ \_. |(_-/(_-/ \ V  V // _ \| '_|/ _` |
   \u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m  |_|   |__/ /__//__/  \_/\_/ \___/|_|  \__/_|
   \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
    \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
     \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
"""

print(logo)

# Asking User for Password Length
print('<Number> for length. \n credits for Credits. \n check for checking the version')
lang = input()

# check for version number and format version into a string
version = subprocess.run('curl https://pastebin.com/raw/8x7dtvaS', capture_output=True).stdout.decode()


# define generate_password function
def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    return password


# if lang is credit show Credits + version
if lang == 'credits':

    # noinspection PyTypeChecker
    print('\n CREDITS: \n Origin Code: Sheesha \n Optimizer: EuGaming \n Version: ' + version + '\n Discord: https://discord.gg/cQAk2etuY3 \n')

elif lang == 'check':

    if version == '1.4.2':
        print('\n \033[1;32;40m up to date!')
    else:

        print('\n \033[31m Update available! \n you a on 1.4 but the newest version is ' + version)
else:
    # Print finished Password if lang was a number
    print('\033[0m Here is the Password: \n \n' + generate_password(int(lang)) + '\n')
