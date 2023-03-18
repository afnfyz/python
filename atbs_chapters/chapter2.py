import random, sys, os, math

from random import * # If this format is used you don't have to call random prefix before function.
for i in range (7):
    print(randint(1,50))

for i in range (5):
    print(random.randint(1,10))


# Comparison Operators

42 == 42
'hi' == 'hi'
'dog' != 'cat'
25 != 22
20 < 23
45 > 25
22 <= 22.0
34 >= 33
not True
not False
print("Hello World!" + " Welcome")

# Flow Control Statements & Code Blocks
name = input("Name: ")
password = input("Password: ")
if name == 'Hamza':
     print('Hello, Hamza')
if password == 'sword':
         print('Access granted.')
else:
         print('Wrong password.')

# If, Elif, Else
# Only prints one of the clauses.
name = 'Maryam'
age = 13
if name == 'Aisha':
    print('Hi, Aisha.')
elif age < 12:
    print('You are not Aisha, kiddo.')
elif age > 2000:
    print('Unlike you, Aisha is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Aisha, grannie.')
else:
    print("Who are you?")

# While Loop
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

spam = 0
while spam < 10:
    print('Hello, world.')
    spam = spam + 1

# Without break clause.
name = ''
while name != 'your name':
       print('Please type your name.')
       name = input()
print('Thank you!')

# With break clause.
while True:
    print("Please input your name: ")
    name = input()
    if name == 'your name':
        break
print ('Thanks!')

# With continue clause. When executed will start the loop from the beginning.
while True:
    print('Who are you?')
    name = input()
    if name != 'Ahmed':
         continue
    print('Hello, Ahmed. What is the password? (It is a fruit.)')
    password = input()
    if password == 'mango':
         break
    print('Access granted.')    

while True:
    print("What is your name?")
    name = input()
    if name != 'Dawud':
     continue
    print("Hello Dawud, please select a number: ")
    num = int(input())
    if num != int(5):
     continue
    print("Welcome Dawud!") 
    break

name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
     print('Be sure to have enough room for all your guests.')
print('Done')

statement="My name is "
for i in range(5):
    print(statement, 'Jimmy Five Times (' + str(i) + ')')

total=0
for num in range(15):
    total = total + num
print(total)

i=0
while i<4:
    print('Jimmy', str(i))
    i += 1

# Range function and step argumants

for a in range(12, 16): # some functions can be called with multiple arguments like range
    print(a)

for b in range(0, 10, 2): # here 2 is the third argument and it called the step argument
    print(b)              # so this function will count from 0 to 10 by intervals of two

for c in range(10, -1, -2): # here the step function is used to count backwards
    print(c)

colors = ["red" "blue", "purple"]
for color in colors:
  print(color)


import sys

while True:
    print("Type exit to exit")
    user_input = input()
    if user_input == "exit":
        sys.exit()
    else:
        print(f"You typed,'{user_input}'.") 
        print("Please type exit to exit.")


import random

print("I am guessing a number between 1 and 25.")

num=random.randint(1,20)

for i in range(1,10):
    print("Take a guess.")
    guess=int(input())
    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guess is too high.")
    else:
        break

if guess == num:
    print("That's correct, you guessed my number in", str(i), "guesses!")
else:
    print("Nope, the number I had in mind was", str(num))