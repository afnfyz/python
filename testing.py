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
