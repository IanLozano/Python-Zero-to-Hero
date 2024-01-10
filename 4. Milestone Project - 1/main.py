import utilities as util

print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' ']*10
    # Do you want to be X or O
    player1_marker, player2_marker = util.player_input()
    # Turn
    turn = util.chose_first()
    print(turn + ' will go first!')
    # Are you ready to play?
    game_on = util.ready()

    while game_on:
        util.display_board(theBoard)
        for i in range(1,10):
            if turn == 'Player 1':
                theBoard=util.next_position(theBoard,player1_marker)
                util.display_board(theBoard)
                turn = 'Player 2'
                if util.check(theBoard,player1_marker):
                    print('Player 1 has won!')
                    game_on=False
                    break
            else:
                theBoard=util.next_position(theBoard,player2_marker)
                util.display_board(theBoard)
                turn = 'Player 1'
                if util.check(theBoard,player2_marker):
                    print('Player 2 has won!')
                    game_on=False
                    break
        else:
            print('The game is a draw!')
            break
            
    if not util.replay():
        print('Thanks for playing!')
        break
