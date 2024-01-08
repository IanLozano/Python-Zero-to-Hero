import utilities as util

print('WELCOME TO THREE CUP MONTE GAME!')

while True:
    mylist=['O','','']
    util.shuffle_list(mylist)
    print(mylist)

    guess=util.player_guess()

    check=util.check_guess(mylist,guess)
    
    wanna_play=util.play_again()
    if wanna_play=='Y':
            continue
    else:
        print('Thanks for playing!')
        break

        




