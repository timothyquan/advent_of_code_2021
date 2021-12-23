import numpy as np
import pandas as pd
from aocd.models import Puzzle
# https://pypi.org/project/advent-of-code-data/

#input = "16,1,2,0,4,2,7,1,2,14"
input = Puzzle(2021, 7).input_data

pos_list = input.split(',')
pos_list = list(map(int, pos_list))

df = pd.DataFrame(pos_list, columns=["start_pos"])
df.sort_values("start_pos", inplace=True, ignore_index=True)
med_idx = round(len(df) / 2)
med = df.start_pos[med_idx]
df[df.start_pos[med_idx]] = df.apply(
    lambda row: abs(row.start_pos - df.start_pos[med_idx]), axis=1)

df = df.append(df.sum(), ignore_index=True)

print(f"The optimal position - mean - to move your octopuses is {med}")
print(f"The fuel used is {df[med][len(df)-1]}")
