import io

def print_board_number ( board_number: tuple) -> str:
    """prints the number and an asterisk if that number has been found"""
    if board_number[1]:
        return f"{board_number[0]:2}*"
    else:
        return f"{board_number[0]:2} "

class bingoboards ():
    def __init__(self) -> None:
        self._boards = list()
        self._winners = list()

    def number_boards (self) -> int:
        return len(self._boards)

    def create_boards (self, board_data: io.IOBase):
        current_board = len(self._boards)
        temp_board = list()
        for boardstr in board_data.readlines():
            board_line = boardstr.strip()
            if len(board_line) == 0: # empty string (used to delinate boards)
                if not temp_board: # no board data
                    continue

                # board contains data so append to board
                if len(temp_board) == 5: # correct number or rows
                    self._boards.append(temp_board)
                else:
                    print("Error: incorrect number of rows -", len(temp_board))
                temp_board = list()
                continue
            
            # read data into board (should be 5 numbers long)
            line = [(int(x), False) for x in board_line.split()]
            if len(line) == 5:
                temp_board.append(line)
            else:
                print("Error: incorrect amount of numbers in row fount -", len(line))

        if temp_board: # board data still to add (no blank line at end of file)
            if len(temp_board) == 5: # correct number or rows
                self._boards.append(temp_board)
            else:
                print("Error: incorrect number of rows -", len(temp_board))

    def print_boards (self):
        print("Boards in play:", len(self._boards))
        for board in self._boards:
            for row in board:
                print(' '.join(map(print_board_number,row)))
            print() # blank line to separate boards

    def check_row_winner (self, board_index: int, row_index: int) -> bool:
        for column in self._boards[board_index][row_index]:
            if column[1] == False:
                return False
        return True # all numbers in row found

    def check_column_winner (self, board_index: int, column_index: int) -> bool:
        for row in self._boards[board_index]:
            if row[column_index][1] == False:
                return False
        return True # all numbers in row found

    def call_number (self, number: int) -> int: # return -1 if winner not found
        winning_board = -1
        for bi, board in enumerate(self._boards):
            for ri, row in enumerate(board):
                if (number,False) in row:
                    position = row.index((number,False))
                    row[position] = (number, True) # tuple doesnt support assignment so replace tuple

                    if bi not in self._winners: # board not already won
                        if self.check_row_winner(bi,ri) or self.check_column_winner(bi,position):
                            self._winners.append(bi)
                            winning_board = bi # cannot return here as it will not mark the number off on subsequent boards - needed for part B
                    continue
        return winning_board

    def board_score (self, board_index: int) -> int:
        total = 0
        for row in self._boards[board_index]:
            total += sum(x[0] for x in row if x[1] == False)
        return total

    def number_winners (self) -> int:
        return len(self._winners)

    def last_winner (self) -> int:
        return self._winners[-1]

def bingo (stream: io.IOBase) -> None:
    bingonumbers = stream.readline().split(',')
    print(len(bingonumbers))
    boards = bingoboards()
    boards.create_boards(stream)
    #boards.print_boards()
    winner = -1
    ballno = 0
    called = 0
    while winner < 0:
        called = int(bingonumbers[ballno])
        winner = boards.call_number(called)
        ballno += 1
    print("Winning board", winner, "with final score", boards.board_score(winner) * called)

    while boards.number_winners() < boards.number_boards() and ballno < len(bingonumbers):
        called = int(bingonumbers[ballno])
        winner = boards.call_number(called)
        ballno += 1

        if winner >= 0:
            print("Next board",winner,"afer",called,"called")

    loser = boards.last_winner()
    print("Losing board", loser, "with final score", boards.board_score(loser) * called)

if __name__ == "__main__":
    testdata = io.StringIO("""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""")
    print("Test data")
    bingo(testdata)

    print("Live data")
    with open("input.txt") as bingodata:
        bingo(bingodata)