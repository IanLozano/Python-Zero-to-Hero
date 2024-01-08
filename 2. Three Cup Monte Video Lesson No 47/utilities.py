from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)

def player_guess():
    guess=''
    while guess not in ('0','1','2'):
        guess=input('Pick a number: 0,1 or 2: ')
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('Congratulations you won!')
    else:
        print("Wrong guess!")

def play_again():
    wanna_play=''
    while wanna_play not in ('Y','N'):
        wanna_play=input('Wanna play again?, Y or N: ').upper()
    return wanna_play