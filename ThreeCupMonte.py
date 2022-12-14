from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
mylist = [' ','O',' ']

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0,1 or 2:')
        if guess not in ['0', '1', '2']:
            print("ERROR, \nPLEASE ENTER NUMBER FROM THE LIST PROVIDED!\n")
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
    else:
        print("Wrong Guess!")
        print(mylist)

mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)