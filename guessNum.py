import random

number = random.randint(0, 10)
i=0
print('Guess the number')
while True:
    guess = int(input())
    if guess < number:
        print ('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('Good job! You guessed the number in ' + str(i) + ' tries.')
        break
    i += 1
