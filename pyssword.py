import string
import random
import requests

# Printing The Logo

print(""""
     \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
    \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m    ___  _  _                                _
   \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[34m-\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m  | _ \| || | ___ ___ _ __ __  ___  _ _  __| |
   \u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m  |  _/ \_. |(_-/(_-/ \ V  V // _ \| '_|/ _` |
   \u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m  |_|   |__/ /__//__/  \_/\_/ \___/|_|  \__/_|
   \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
    \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[33m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m
     \u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m\u001b[36m#\u001b[0m 
""")

# Asking User for Password Length
print(' <Number> for length. \n credits for Credits. \n check for checking the version \n')
lang = input()

# check for version number and format version into a string

headers = {'User-Agent': 'curl/7.64.1'}
version = requests.post('https://pastebin.com/raw/8x7dtvaS', headers=headers)


# define generate_password function
def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters+string.digits+str('?')+str('!')+str('*')+str('#')+str('&')) for _ in range(length))
    return password


# if lang is credit show Credits + version
if lang == 'credits':

    # noinspection PyTypeChecker
    print('\n CREDITS: \n Origin Code: Sheesha \n Optimizer: EuGaming \n Version: ' + version.content + '\n Discord: TERMINATED \n')

elif lang == 'check':

    if version.content == '1.4.3':
        print('\n \033[1;32;40m up to date!')
    else:

        versionraw = version.content
        print('\n \033[31m Update available! \n you a on 1.4.2 but the newest version is ' + str(versionraw))
else:
    # Print finished Password if lang was a number
    print('\n \033[0m Here is the Password: \n \n' + generate_password(int(lang)) + '\n')


