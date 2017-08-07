# import random method first
# default input value is string. you should change the type of variable to int
# you can use print( variable, type(variable)) to control type

import random
print('--------------------------')
print('     Guess number Game')
print('--------------------------')
print()


the_number = random.randint(0, 100)

guess = -1

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')

    guess = int(guess_text)

    if guess < the_number:
        print("too low")

    elif guess > the_number:
        print('too high')

    else:
        print("you win!")

print('done')