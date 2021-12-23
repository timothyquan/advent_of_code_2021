import numpy as np
import pandas as pd
from aocd.models import Puzzle
# https://pypi.org/project/advent-of-code-data/

# input = "16,1,2,0,4,2,7,1,2,14"
input = Puzzle(2021, 7).input_data
pos_list = input.split(',')
pos_list = list(map(int, pos_list))


# part 1===============================================s
df = pd.DataFrame(pos_list, columns=["start_pos"])
df.sort_values("start_pos", inplace=True, ignore_index=True)
med_idx = round(len(df) / 2)
med = df.start_pos[med_idx]
df[df.start_pos[med_idx]] = df.apply(
    lambda row: abs(row.start_pos - df.start_pos[med_idx]), axis=1)

df = df.append(df.sum(), ignore_index=True)

print(
    f"The optimal position - the median starting position - to move your octopuses is {med}")
print(f"The fuel used is {df[med][len(df)-1]}")


# part 2===============================================
df = pd.DataFrame(pos_list, columns=["start_pos"])
df.sort_values("start_pos", inplace=True, ignore_index=True)
average = round(df.start_pos.mean())

for i in range(average - 5, average + 5, 1):
    df[f'moves_to_{i}'] = df.apply(
        lambda row: abs(row.start_pos - i), axis=1)

for i in range(average - 5, average + 5, 1):
    df[f'fuel_usage_to_{i}'] = df.apply(lambda row: (
        row[f'moves_to_{i}']*(row[f'moves_to_{i}']+1)) / 2, axis=1)


sums = df.sum()[11:]
optimal_move = sums.idxmin()
optimal_move = optimal_move[len(optimal_move)-3:]
optimal_fuel = sums.min()
print(
    f"The optimal position to move your octopuses is {optimal_move}")
print(f"The fuel used is {optimal_fuel}")
