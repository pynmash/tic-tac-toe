class Board:
    def __init__(self):
        self.board = [[' . ', ' . ', ' . '], [' . ', ' . ', ' . '], [' . ', ' . ', ' . ']]

    def show(self):
        print()
        top_row = [' 1 ', ' 2 ', ' 3 ']
        print(" ", " ".join(top_row))
        for row in enumerate(self.board):
            print(row[0] + 1, '|'.join(row[1]))
            if row[0] < len(self.board) -1:
                print('  -----------')
        print()


if __name__ == '__main__':
    board = Board()
    board.show()