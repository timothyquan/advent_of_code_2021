from aocd.models import Puzzle
import pandas as pd
import pprint as pp


class Octo_Grid:
    def __init__(self, input):
        lines = input.splitlines()
        line = [list(l) for l in lines]

        self.df_grid = pd.DataFrame(line)
        self.coord_dict = {}
        self.octoval_list = [set() for i in range(10)]

        for ridx, l in enumerate(line):
            for cidx, c in enumerate(l):
                self.coord_dict[(ridx, cidx)] = int(c)
                self.octoval_list[int(c)].add((ridx, cidx))

    def update_octo(self, coord, val):
        old_val = self.coord_dict[coord]
        self.coord_dict[coord] = val
        self.octoval_list[old_val].remove(coord)
        self.octoval_list[val].add(coord)

    def step_all(self):
        shifted = [set() for i in range(10)]
        for i, s in enumerate(self.octoval_list):
            shifted =

    def update_df(self):
        for c in self.coord_dict.keys():
            self.df_grid.loc[c] = self.coord_dict[c]
        pp.pprint(self.df_grid)
        print(self.coord_dict)
        [print(f"Energy {i}: {s}") for i, s in enumerate(self.octoval_list)]


if __name__ == "__main__":
    with open('./day_11/sample_input.txt') as f:
        lines = f.read()

    octos = Octo_Grid(lines)
    octos.update_df()
    #octos.update_octo((0, 4), 9)

    octos.step_all()
