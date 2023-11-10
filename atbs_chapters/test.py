name = 'Yusuf'
password = 'Egypt'

print('What is your username?')
uname = input()

while name != uname:
    print('wrong username, please try again')
    uname = input()
    
else:
    print('Input your password')
    upassword = input()

    while password != upassword:
        print('Incorrect password. Try again.')
        upassword = input()

print('Login successful!')