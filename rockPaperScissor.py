import random, sys

print('ROCK, PAPER, SCISSORS')

win = 0
loss = 0
tie = 0

while True:
    #Displaying the stats
    print(str(win) + ' Wins,' + str(loss) + ' Losses,' + str(tie) +' Ties')

    #Getting the move
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()

    #Quiting the program
    if playerMove == 'q':
        sys.exit()

    #Display the move
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    #Computer move
    cmpMove = random.randint(1, 3)
    #Displaying the Computer move
    if cmpMove == 1:
        cmpMove = 'r'
        print('ROCK')
    elif cmpMove == 2:
        cmpMove = 'p'
        print('PAPER')
    elif cmpMove == 3:
        cmpMove = 's'
        print('SCISSORS')

    #checking the result
    if playerMove == cmpMove:
        print('Its a tie!')
        tie += 1
    elif playerMove == 'r' and cmpMove == 'p':
        print('You lose!')
        loss += 1
    elif playerMove == 'r' and cmpMove == 's':
        print('You win!')
        win += 1
    elif playerMove == 'p' and cmpMove == 'r':
        print('You win!')
        win += 1
    elif playerMove == 'p' and cmpMove == 's':
        print('You lose!')
        loss += 1
    elif playerMove == 's' and cmpMove == 'r':
        print('You lose!')
        loss += 1
    elif playerMove == 's' and cmpMove == 'p':
        print('You win!')
        win += 1
