# 1. Set up players
# 2. set up board
# 3. Get move from player
# 4. Check for winner
# 5. Switch player

from player import Player
from board import Board

def round():
    board = Board()
    board.show()

if __name__ == "__main__":
    # Init players
    player1 = Player('Dan', 'X')
    player2 = Player('John', 'O')
    round()