import pandas as pd
from aocd.models import Puzzle


# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
puzzle_input = Puzzle(year=2021, day=3).input_data
input = [i for i in puzzle_input.split('\n')]
# input = ['00100',
#          '11110',
#          '10110',
#          '10111',
#          '10101',
#          '01111',
#          '00111',
#          '11100',
#          '10000',
#          '11001',
#          '00010',
#          '01010']


def binarylist_to_decimal(bitlist):
    pwr = 0
    dec = 0
    for i in range(len(bitlist)-1, -1, -1):
        dec += bitlist[i] * pow(2, pwr)
        pwr += 1
    return dec


bit_list = []
for i in input:
    bit_list.append([c for c in i])

df = pd.DataFrame(bit_list)

gammalist = [int(c) for c in (df.mode().values.tolist()[0])]
epsilonlist = [(int(c) - 1) * -1 for c in gammalist]

print(f'The gamma rate is {gammalist} and the epsilon rate is {epsilonlist}.')
print(
    f'The power consumption of the submarine is {binarylist_to_decimal(gammalist) * binarylist_to_decimal(epsilonlist)}.')
