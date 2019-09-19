# Rock, Scissors and Paper Game
import random
# input
def player():
    user = input("Type rock, scissors or paper: ")
    return user
# compute the random number assign to a choice
def cpu():
    comp = random.randint(0,2)
    if comp == 0:
        comp = 'rock'
    elif comp == 1:
        comp = 'scissors'
    else:
        comp = 'paper'
    return comp
# check Winner
while True:
    print("")
    user = player()
    comp = cpu()
    print("")
    if user == 'rock':
        if comp == 'rock':
            print('Draw!')

        elif comp == 'scissors':
            print('You win!')

        elif comp == 'paper':
            print('cpu win!')

    elif user == 'scissors':
        if comp == 'scissors':
            print('Draw!')
        elif comp == 'rock':
            print('cpu win!')

        elif comp == 'paper':
            print('You Win!')

    elif user == 'paper':
        if comp == 'paper':
            print('Draw')
        elif comp == 'rock':
            print('cpu win !')

        elif comp == 'scissors':
            print('cpu win!')
# keep Trying
    keep_going = input("do you want to try again(Enter y for yes and press any key to quit)")
    if keep_going == 'y':
        pass
    else:
        quit()
