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
'''
