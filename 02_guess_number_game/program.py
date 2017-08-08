# import random method first
# default input value is string. you should change the type of variable to int
# you can use print( variable, type(variable)) to control type

import random

print('--------------------------')
print('     Guess number Game')
print('--------------------------')
print()

the_number = random.randint (0, 100)

guess = -1

name = input ('What is your name Player? ')

while guess != the_number:

    guess_text = input ('Guess a number between 0 and 100: ')

    guess = int (guess_text)

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW'.format (name, guess))

    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH'.format (name, guess))


    else:
        print('Excellent work {}, you won, it was {}'.format (name, guess))

print('done')
