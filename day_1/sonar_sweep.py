__author__ = "Tim Quan"


# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=1)


# parsing input - dr = depth readings
dr = [int(i) for i in puzzle.input_data.split('\n')]

# part 1:---------------------------------------


def count_increases(intlist):
    """Takes an intlist - list of integers -
    returns the count of consecutive increases within said list"""
    cnt = 0
    for i in range(1, len(intlist)):
        cnt += (intlist[i] > intlist[i-1])
    return cnt


print(f'Counted {count_increases(dr)} depth increases.')

# part 2:---------------------------------------
window_size = 3

# make sure we dont count any trailing incomplete windows - round down to the the highest number divisible by 3
last_iter = window_size * int(len(dr) / window_size)

# make make a list of list chunked into [window_size]
windowed_drs = [dr[i:(i+window_size)]
                for i in range(0, last_iter, 1)]

summed_windows = [sum(window) for window in windowed_drs]
print(f'Counted {count_increases(summed_windows)} depth increases with 3 measurement sliding windows.')
