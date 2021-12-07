__author__ = "Tim Quan"

# reading input file
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(f'{dir_path}\input.txt')
depth_readings = [int(i) for i in input_file.readlines()]


cnt = 0
for i in range(depth_readings.__len__()):
    cnt += (depth_readings[i] > depth_readings[i-1])

print(f'Counted {cnt} depth increases.')
