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

        # columns
        for column in zip(*self.board):
            if "   " in column:
                continue
            elif len(set(column)) == 1:
                return "win"

        # Diagonals
        all_cells = [item for lst in self.board for item in lst]
        diagonals = [[all_cells[0], all_cells[4], all_cells[8]],[all_cells[2], all_cells[4], all_cells[6]]]
        for diagonal in diagonals:
            if "   " in diagonal:
                continue
            elif len(set(diagonal)) == 1:
                return "win"
        # Top left to bottom right
        # if all_cells[0] == all_cells[4] and all_cells[4] == all_cells[8]:
        #     return "win"
        
        # # Top right to bottom left
        # if all_cells[2] == all_cells[4] and all_cells[4] == all_cells[6]:
        #     return "win"

        # no spaces left
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