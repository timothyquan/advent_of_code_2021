from aocd.models import Puzzle

import pprint as pp
import pandas as pd
import sys


class Basin_Map:
    def __init__(self, lines):
        line_list = lines.split('\n')
        grid = [list(l) for l in line_list]
        self.df_grid = pd.DataFrame(grid).astype('int32')
        lowgrid = [[True for c in l] for l in line_list]
        self.df_lowgrid = pd.DataFrame(lowgrid)
        lowgrid = [[False for c in l] for l in line_list]
        self.basin_grid = pd.DataFrame((lowgrid))
        self.basin_dict = {}
        self.low_points = []

    def detect_lowpoint(self, loc):
        adjs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for a in adjs:
            nghbr = tuple([loc[i]+a[i] for i in range(2)])
            try:
                if self.df_grid.loc[loc] >= self.df_grid.loc[nghbr]:
                    self.df_lowgrid.loc[loc] = False
            except KeyError:
                pass

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
            for i in lowlist.index:
                self.low_points.append((i, c))
        return count

    def define_basin(self, loc, parentloc=False):
        if not parentloc:
            parentloc = loc
            self.basin_dict[loc] = set()
        adjs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.basin_grid.loc[loc] = True
        for a in adjs:
            nghbr = tuple([loc[i]+a[i] for i in range(2)])
            try:
                if self.df_grid.loc[loc] <= self.df_grid.loc[nghbr] and self.df_grid.loc[nghbr] < 9:
                    if not nghbr in self.basin_dict[parentloc]:
                        self.basin_dict[parentloc].add(nghbr)
                        self.basin_grid.loc[nghbr] = True
                        self.define_basin(nghbr, parentloc)
            except KeyError as err:
                # print(err)
                pass
        return self.basin_dict

    def display(self):
        print("Number map/grid: ")
        pp.pprint(self.df_grid)
        print("Lowpoint map/grid: ")
        pp.pprint(self.df_lowgrid)
        print("Basin map/grid: ")
        pp.pprint(self.basin_grid)
        pp.pprint(self.df_grid[15:18])

    def detect_basins(self):
        for low in self.low_points:
            self.define_basin(low)
        return self.basin_dict


if __name__ == '__main__':
    with open('./day_09/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 9).input_data
    bm = Basin_Map(lines)
    bm.detect_lowpoints()
    print(
        f"The sum of the risk levels of all low points is {bm.return_lowpoints_sum()}.")

    print("Part 2===========================")
    basin_dict = bm.detect_basins()
    basin_sizes = sorted(
        [len(basin_dict[b]) + 1 for b in basin_dict], reverse=True)
    print(f"These is the sizes of  the basins: {basin_sizes}")
    print(
        f"This is the 3 largest basins multiplied together: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")
