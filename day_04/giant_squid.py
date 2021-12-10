import pandas as pd
import numpy as np
import pprint as pp
from aocd.models import Puzzle


class Bingo_Board:
    def __init__(self, df):
        self.df_num = df.copy()
        grid = np.reshape([False for i in range(25)], (5, 5))
        self.df_marks = df.copy()
        lines = [0 for i in range(10)]
        self.srs_lines = pd.Series(lines)

    def call(self, num):
        for col in self.df_num:
            column = self.df_num[col]
            found = column[column == num]

            if len(found) > 0:
                self.df_marks.at[found.index[0], col] = False
                self.srs_lines[col] += 1
                self.srs_lines[found.index[0]+5] += 1

    def bingo_check(self):
        return len(self.srs_lines[self.srs_lines > 4]) > 0

    def print_board(self):
        pp.pprint(self.df_num)
        pp.pprint(self.df_marks)

    def unmarked_sum(self):
        sum = 0
        df = self.df_marks.astype('int32', copy=True)
        for c in df:
            sum += int(df[c].sum())
        return sum


class Bingo_Game:
    def __init__(self, input_string):
        input_list = input_string.split('\n\n')
        call_order = input_list[0].split(',')
        boards = []
        for i in input_list[1:]:
            board = pd.DataFrame(np.reshape(i.split(), (5, 5)))
            boards.append(board)

        self.bbs = [Bingo_Board(b) for b in boards]
        self.call_order = call_order

    def sequential_result(self):
        bingod = False
        last_call = 0
        winner = ''
        for c in self.call_order:
            for b in self.bbs:
                b.call(c)
                if b.bingo_check():
                    bingod = True
                    winner = b
                    last_call = int(c)
                    break
            if bingod:
                break
        return winner, last_call


if __name__ == "__main__":
    input = Puzzle(2021, 4).input_data
#     input = "\
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\
# \n\
# 22 13 17 11  0\n\
#  8  2 23  4 24\n\
# 21  9 14 16  7\n\
#  6 10  3 18  5\n\
#  1 12 20 15 19\n\
# \n\
#  3 15  0  2 22\n\
#  9 18 13 17  5\n\
# 19  8  7 25 23\n\
# 20 11 10 24  4\n\
# 14 21 16 12  6\n\
# \n\
# 14 21 17 24  4\n\
# 10 16 15  9 19\n\
# 18  8 23 26 20\n\
# 22 11 13  6  5\n\
#  2  0 12  3  7"

    first_game = Bingo_Game(input)
    winner, last_call = first_game.sequential_result()
    print(f"Here's the winner, the last call was {last_call}:")
    winner.print_board()
    print(
        f'The final score was {int(last_call) * int(winner.unmarked_sum())}.')
