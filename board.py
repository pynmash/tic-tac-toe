class Board:
    def __init__(self):
        self.board = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]

    def show(self):
        print()
        top_row = [' 1 ', ' 2 ', ' 3 ']
        print(" ", " ".join(top_row))
        for row in enumerate(self.board):
            print(row[0] + 1, '|'.join(row[1]))
            if row[0] < len(self.board) -1:
                print('  -----------')
        print()

    def check_win(self):
        spaces_left = False
        # rows
        for row in self.board:
            if "   " in row:
                spaces_left = True
                continue
            elif len(set(row)) == 1:
                return "win"
        if not spaces_left:
            return 'draw'
        return False
        

    
    def move(self, player, coordinates):
        if self.board[coordinates[0]][coordinates[1]] == '   ':
            self.board[coordinates[0]][coordinates[1]] = f' {player.mark} '
            return True
        else:
            return False



if __name__ == '__main__':
    board = Board()
    board.show()