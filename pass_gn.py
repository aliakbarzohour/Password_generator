# start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import Library -----------------------------------
import random
from colorama import init, Fore
init()
# login --------------------------------------------
print('Welcome To your Password Generator !')
# chars --------------------------------------------
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'
# promts -------------------------------------------
number = input(Fore.MAGENTA+' [%] '+Fore.WHITE+'Amount of password to generate: ')
number = int(number)

length = input(Fore.MAGENTA+' [*] '+Fore.WHITE+'input your password length: ')
length = int(length)
# print status -------------------------------------
print(Fore.WHITE+'\nHere are Your Passwords: ')
# loop ---------------------------------------------
for pwd in range(number):
    passwords = Fore.GREEN+" [+] " + Fore.WHITE+''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

# end <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
