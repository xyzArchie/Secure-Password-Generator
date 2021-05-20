import colorama
from os import system
from time import sleep
from random import choice
from os import system, _exit
from string import ascii_letters, digits, punctuation
from colorama import Fore, Back, Style

system('cls && title Password Generator - By @Astivery')

print(Fore.CYAN + '''

 ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ██· █▌▐█▪     ▀▄ █·██▪ ██     ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
 ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██     ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
.▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀                                                       
''')

while True:
    note = str(input('Note: '))
    email = str(input('Email: '))
    password = str(input('Password: '))
    with open('Passwords.txt', 'a', encoding='UTF-8') as f:
        f.write('Note: %s\nEmail / Username: %s\nPassword: %s\n\n' % (note, email, password))
    print()
