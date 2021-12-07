__author__ = "Tim Quan"

# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=1)

# parsing input
depth_readings = [int(i) for i in puzzle.input_data.split('\n')]

# part 1:---------------------------------------
cnt = 0
for i in range(0, depth_readings.__len__()):
    cnt += (depth_readings[i] > depth_readings[i-1])

print(f'Counted {cnt} depth increases.')

# part 2:---------------------------------------
