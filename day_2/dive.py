# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=2)

input = [i for i in puzzle.input_data.split('\n')]
# input = ['forward 5',
#          'down 5',
#          'forward 8',
#          'up 3',
#          'down 8',
#          'forward 2']
input_map = {'forward': 0,
             'up': 1,
             'down': 2}


xyy = [0, 0, 0]
for i in input:
    ax, mv = i.split(' ')
    xyy[input_map[ax]] += int(mv)

print(f'The horizontal position is {xyy[0]} and the depth is {xyy[2]-xyy[1]}.')
print(
    f'The result of multiplying the two together is {xyy[0] * (xyy[2]-xyy[1])}.')
