from aocd.models import Puzzle

import pprint as pp
import pandas as pd


class Basin_Map:
    def __init__(self, lines):
        line_list = lines.split('\n')
        grid = [list(l) for l in line_list]
        self.df_grid = pd.DataFrame(grid).astype('int32')
        lowgrid = [[True for c in l] for l in line_list]
        self.df_lowgrid = pd.DataFrame(lowgrid)

    def detect_lowpoint(self, loc):
        adjs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        if loc == (95, 10):
            print('wtf')
        for a in adjs:
            nghbr = tuple([loc[i]+a[i] for i in range(2)])
            try:
                if self.df_grid.loc[loc] >= self.df_grid.loc[nghbr]:
                    self.df_lowgrid.loc[loc] = False
            except KeyError:
                pass
                # print(f"{loc} is on the edge, {nghbr} does not exist.")

    def detect_lowpoints(self):
        for y in self.df_grid.index:
            for x in self.df_grid.columns:
                self.detect_lowpoint((y, x))

    def return_lowpoints_sum(self):
        count = 0
        for c in self.df_lowgrid:
            lowlist = self.df_grid[c][self.df_lowgrid[c] == True]
            for i in lowlist:
                count += int(i) + 1

        return count

    def display(self):
        pp.pprint(self.df_grid)
        pp.pprint(self.df_lowgrid)


if __name__ == '__main__':
    pass
    with open('./day_09/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 9).input_data
    bm = Basin_Map(lines)
    bm.detect_lowpoints()
    bm.display()
    print(
        f"The sum of the risk levels of all low points is {bm.return_lowpoints_sum()}.")
