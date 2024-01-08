import os
import utilities as util

game_list=[0,1,2]
game_on=True
while game_on:
    # Clear the screen
    os.system('cls')
    # Display the game
    util.display_game(game_list)
    # Pick a position to replace (0,1,2)
    position=util.position_choice()
    # Replace the player_string in the list
    game_list=util.replacement_choice(game_list,position)
    # Clear the screen
    os.system('cls')
    # Display the game
    util.display_game(game_list)
    game_on=util.gameon_choice()