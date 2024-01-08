def display_game(game_list):
    print('Here is the current list:')
    print(game_list)

def position_choice():
    choice='WRONG'
    while choice not in ('0','1','2'):
        choice=input('Pick a position to replace (0,1,2): ')
        if choice not in ('0','1','2'):
            print('Sorry, but you did not choose a valid position (0,1,2)')
    return int(choice)

def replacement_choice(game_list,position):
    user_replacement=input('Type a string to place at position: ')
    game_list[position]=user_replacement
    return game_list

def gameon_choice():
    choice='WRONG'
    while choice not in ('Y','N'):
        choice=input('Would you like to keep playing? Y or N: ').upper()
        if choice not in ('Y','N'):
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice=='Y':
        return True
    else:
        print('Thanks for playing!')
        return False
    