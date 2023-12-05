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