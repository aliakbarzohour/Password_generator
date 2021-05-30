# start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import Library -----------------------------------
import random
# login --------------------------------------------
print('Welcome To your Password Generator !')
# chars --------------------------------------------
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'
# promts -------------------------------------------
number = input('Amount of password to generate: ')
number = int(number)

length = input('input your password length: ')
length = int(length)
# print status -------------------------------------
print('\nhere are your passwords: ')
# loop ---------------------------------------------
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

# end <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<