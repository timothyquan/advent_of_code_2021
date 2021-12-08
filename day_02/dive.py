# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=2)

input = [i for i in puzzle.input_data.split('\n')]

# part 1: ---------------------------------------------------------
input_map = {'forward': 0,
             'up': 1,
             'down': 2}


xyy = [0, 0, 0]
for i in input:
    ax, mv = i.split(' ')
    xyy[input_map[ax]] += int(mv)

print('Part 1: -----------------------------------------------------')
print(f'The horizontal position is {xyy[0]} and the depth is {xyy[2]-xyy[1]}.')
print(
    f'The result of multiplying the two together is {xyy[0] * (xyy[2]-xyy[1])}.')
# ------------------------------------------------------------------


# part 2: ---------------------------------------------------------

# x, y, aim
curpos = [0, 0, 0]
for i in input:
    xyy = [0, 0, 0]
    ax, mv = i.split(' ')
    xyy[input_map[ax]] += int(mv)
    curpos[0] += xyy[0]
    curpos[2] -= xyy[1]
    curpos[2] += xyy[2]
    curpos[1] += curpos[2] * xyy[0]

print('Part 2: -----------------------------------------------------')
print(f'The horizontal position is {curpos[0]} and the depth is {curpos[1]}.')
print(
    f'The result of multiplying the two together is {curpos[0] * (curpos[1])}.')
# ------------------------------------------------------------------
