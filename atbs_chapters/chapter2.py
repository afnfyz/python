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
    print(statement + 'Jimmy Five Times (' + str(i) + ')')
