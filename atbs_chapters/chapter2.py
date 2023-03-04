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

# Only prints one or none of the clauses.
name = 'Zaynab'
age = 3000
if name == 'Zaynab':
    print('Hi, Zaynab.')
elif age < 12:
    print('You are not Aisha, kiddo.')
elif age > 2000:
    print('Unlike you, Aisha is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Aisha, grannie.')