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
        return (len(found) > 0)

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
    def __init__(self, input_string, play_through=False):
        input_list = input_string.split('\n\n')
        call_order = input_list[0].split(',')
        boards = []
        for i in input_list[1:]:
            board = pd.DataFrame(np.reshape(i.split(), (5, 5)))
            boards.append(board)

        self.bbs = [Bingo_Board(b) for b in boards]
        self.call_order = call_order
        self.play_through = play_through

    def call_all_boards(self, num):
        poplist = []
        for idx, b in enumerate(self.bbs):
            b.call(num)
            if b.bingo_check():
                if not self.play_through:
                    return b
                else:
                    if len(self.bbs) > 1:
                        poplist.append(idx)
                    else:
                        return b
        for i in sorted(poplist, reverse=True):
            self.bbs.pop(i)
        return False

    def make_calls(self):
        call = self.call_order[0]
        winner = self.call_all_boards(call)
        self.call_order.pop(0)
        if winner:
            return call, winner
        if len(self.call_order) > 0:
            return self.make_calls()
        return False

    def play_game(self, iter=0):
        last_call, winner = self.make_calls()
        print(
            f"The last number called was {last_call}, here's the winning board:")
        winner.print_board()
        print(
            f'The final score was {int(last_call) * int(winner.unmarked_sum())}.')


if __name__ == "__main__":
    input = Puzzle(2021, 4).input_data

    first_game = Bingo_Game(input)
    first_game.play_game()

    last_game = Bingo_Game(input, play_through=True)
    last_game.play_game()
