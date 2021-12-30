from aocd.models import Puzzle
import pandas as pd
import pprint as pp


class Octo_Grid:
    def __init__(self, input):
        self.flash_cnt = 0
        lines = input.splitlines()
        self.grid = [[Octo(int(p), self, (y, x)) for x, p in enumerate(
            list(l))] for y, l in enumerate(lines)]

        self.step_cnt = 0
        self.step_flash_cnt = 0

    def step_all(self):
        self.step_cnt += 1
        self.step_flash_cnt = 0
        [[octo.step() for octo in y] for y in self.grid]

    def step_range(self, yrange, xrange):
        [[octo.step() for octo in y[xrange]] for y in self.grid[yrange]]

    def print_grid(self):
        printable = []
        printable = [[octo.get_pwr() for octo in y] for y in self.grid]
        print(f"Step {self.step_cnt}-=-=-=-=-=-=-=-=-=-=-=-")
        pp.pprint(printable)

    def add_flash(self):
        self.flash_cnt += 1
        self.step_flash_cnt += 1

    def check_sync(self):
        return self.step_flash_cnt == (len(self.grid) * len(self.grid[0]))


class Octo:
    def __init__(self, pwr, grid, coord):
        self.pwr = pwr
        self.last_flashed = -1
        self.grid = grid
        self.coord = coord

    def get_pwr(self):
        return self.pwr

    def step(self):
        if self.last_flashed == self.grid.step_cnt:
            self.pwr = 0
        elif (self.pwr == 9):
            self.last_flashed = self.grid.step_cnt
            self.flash()
            self.pwr = 0
        else:
            self.pwr += 1

    def flash(self):
        y, x = self.coord
        lastrow = (y-1) if (y-1 >= 0) else y
        nextrow = (y+1) if (y + 1 < len(self.grid.grid)) else y
        lastcol = (x-1) if (x-1 >= 0) else x
        nextcol = (x+1) if (x+1 < len(self.grid.grid)) else x
        self.grid.add_flash()

        self.grid.step_range(slice(lastrow, nextrow+1),
                             slice(lastcol, nextcol+1))


if __name__ == "__main__":
    with open('./day_11/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 11).input_data
    steps = 100
    synced = False
    synccnt = 0

    octos = Octo_Grid(lines)
    octos.print_grid()

    for i in range(steps):
        octos.step_all()
        synced = octos.check_sync()
        if not synced:
            synccnt += 1
        octos.print_grid()

    print(f"There have been {octos.flash_cnt} flashes during {steps} steps.")

    while not synced:
        octos.step_all()
        synced = octos.check_sync()
        synccnt += 1

    print(
        f"There were {synccnt} steps before we achieved full syncronization.")
