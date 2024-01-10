import os
import random

def display_board(lst):
    os.system('cls')
    print('   |   |')
    print(' '+lst[7]+' | '+lst[8]+' | '+lst[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+lst[4]+' | '+lst[5]+' | '+lst[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+lst[1]+' | '+lst[2]+' | '+lst[3])
    print('   |   |')

def player_input():
    marker=''
    while marker not in ('X','O'):
        marker=input('Player 1: Do you want to be X or O? ').upper()
        if marker not in ('X','O'):
            print('Wrong choice! Please try again')
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def chose_first():
    if random.randint(0,1)==0:
        return 'Player 2'
    else:
        return 'Player 1'

def ready():
    play_game='Wrong'
    while play_game not in ('Y','N'):
        play_game = input('Are you ready to play? Enter Y or N.').upper()
    if play_game=='Y':
        return True
    else:
        return False

def next_position(lst,marker):
    position='Wrong'
    valid_positions = ['1','2','3','4','5','6','7','8','9']
    while position not in valid_positions:
        position = input('Choose your next position: (1-9): ')
        if position not in valid_positions:
            print('Out of range!')
        else:
            if lst[int(position)]!=' ':
                position='Wrong'
            else:
                lst[int(position)]=marker
                return lst

def check(lst,marker):

    return lst[1]==lst[2]==lst[3]==marker or lst[4]==lst[5]==lst[6]==marker or lst[7]==lst[8]==lst[9]==marker or lst[1]==lst[4]==lst[7]==marker or lst[2]==lst[5]==lst[8]==marker or lst[3]==lst[6]==lst[9]==marker or lst[1]==lst[5]==lst[9]==marker or lst[3]==lst[5]==lst[7]==marker

def replay():
    choice='Wrong'
    while choice not in ('Y','N'):
        choice=input('Wanna play again! Enter Y or N. ').upper()
    return choice=='Y'