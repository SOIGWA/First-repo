
print('WELCOME TO THE ARCADE!')
print('This is a collection of games you can play.\n')
print('please choose a game to play:\n1. Guessing Game\n2. Rock Paper Scissors\n3. Exit')
game_choice = input('Enter your choice (1-3): ')
if game_choice == '1':
    print('You chose Guessing Game!')
    import Guess_Game
    Guess_Game.guessing_game()
elif game_choice == '2':
    print('You chose Rock Paper Scissors!')
    import Rockpaperscissors
    Rockpaperscissors.play_rps()
else:
    print('Exiting the arcade. Goodbye!')