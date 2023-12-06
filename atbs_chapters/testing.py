'''
# While Loop Example
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
    if name == 'afnan':
        print('Hello Afnan!')
        break
print('Thank you')

'''

'''
# While True Loop Example
while True:
    print('Please type your name')
    name = input()
    if name == 'afnan':
        print('Hello Afnan!')
        break
print('Thank you')
'''

'''
# Continue & Break Example
while True:
    print('What is your name?')
    name = input()
    if name != 'Musa':
        continue
    print('Welcome Musa. What is in your hand?')
    response = input()
    if response != 'My staff':
        continue
    break
print('Thank you Musa.')
'''
'''
# For Loop Examples
print ('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))


total = 0
for num in range(101):
    total = total + num
print(total)


print('My name is')
i = 0
while i < 5:
    print('Abdullah Five Times ' + str(i))
    i = i + 1

for i in range(7,17):
    print(i)


for i in range (1,15,3):
    print(i)


for i in range (15,0,-1):
    print(i)

import random
for i in range(5):
    print(random.randint(1,10))

from random import *
for i in range(5):
    print(randint(1,10))
'''

'''
# Sys Exit Example
import sys

while True:
    print('Type exit to exit')
    r = input()
    if r == 'exit':
        sys.exit()
    print('You typed ' + r + '.')
'''
'''
import random

guess = random.randint(1,5)

print('I am thinking of a number between 1 and 5')
user = 0

while user != guess:
    user = int(input('Take a guess:'))
print('That is correct, my guess was' + ' ' + str(guess))
'''
'''
# Guess The Number Program
import random
num = random.randint(1,15)
print('I am thinking of a number between 1 and 15.')
for i in range(1,6):
    guess = int(input('Take a guess:'))
    
    if guess > num:
        print('Your guess is too high')
    elif guess < num:
        print('Your guess is too low')
    else:
        break
if guess == num:
    print('Good Job! My guess was ' + str(num) + '\nYou guessed in ' + str(i) + ' guesses')
else:
    print('Nice try, my guess was ' + str(num))
'''

'''
# Functions

def hello():
    print('Hello!')
    print('Good day!')
    print('Take care!')
hello()
hello()


def hello(name):
    print('Hello, ' + name)

hello('Yusuf')
hello('Yunus')

'''

import random

def getnum(answernumber):
    if answernumber == 1:
        return 'Surah Fatiha'
    elif answernumber == 2:
        return 'Surah Baqarah'
    elif answernumber == 3:
        return 'Surah Aal-e-Imran'
    elif answernumber == 4:
        return 'Surah Nisa'
r = random.randint(1, 4)
surah = getnum(r)
print(surah)