# 1. Set up players
# 2. set up board
# 3. Get move from player
# 4. Check for winner
# 5. Switch player

from player import Player
from board import Board
from random import choice

def round():
    game = True
    starting_player = choice((player1, player2))
    current_player = starting_player
    print(f'Player {starting_player.name} will go first')
    board = Board()
    board.show()
    while game:
        while True:
            try:
                player_move = input('Please enter the coordinates of the space you want to mark. e.g. 13 would be row 1, column 3 (top right): ')
                coords = [int(item)-1 for item in player_move]
                if len(coords) != 2:
                    print("Wrong amount of numbers!")
                    continue
                if not board.move(current_player, coords):
                    print('That spot is already taken!')
                    continue
            except (IndexError, ValueError):
                print('Please make sure you entered the numbers correctly')
                continue
            board.show()
            if current_player.mark == 'X':
                current_player = player2
            else:
                current_player = player1
            print(f"\nIt's {current_player.name}'s turn")

if __name__ == "__main__":
    # Init players
    print('Welcome to TIC-TAC-TOE')
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")
    if player1_name == "":
        player1_name = 'X'
    if player2_name == "":
        player2_name = 'O'
    player1 = Player(player1_name.upper(), 'X')
    player2 = Player(player2_name.upper(), 'O')
    print(f'Round 1: {player1.name} VS {player2.name}')
    round()