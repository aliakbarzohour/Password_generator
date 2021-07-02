# start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import Library -----------------------------------
import random
from colorama import init, Fore

init()
# login --------------------------------------------
print(Fore.RED+'Welcome To your Password Generator !')
# chars --------------------------------------------
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'
# promts -------------------------------------------
number = input('Amount of password to generate: ')
number = int(number)

length = input('input your password length: ')
length = int(length)
# print status -------------------------------------
print(Fore.WHITE+'\nHere are Your Passwords: ')
# loop ---------------------------------------------
for pwd in range(number):
    passwords = Fore.GREEN+"#!#   " + ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

# end <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
