import pandas as pd
import pprint as pp
import numpy as np
from aocd.models import Puzzle
from collections import Counter

# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/


class Vent_Map:
    def __init__(self, input_string):
        line_list = input_string.replace(
            ' -> ', ',', ).replace('\n', ',').split(',')
        line_list = list(map(int, line_list))
        top = max(line_list) + 1
        line_list = [line_list[i:i+2] for i in range(0, len(line_list), 2)]
        line_list = [line_list[i:i+2] for i in range(0, len(line_list), 2)]
        self.line_list = line_list
        # pp.pprint(line_list)
        fill = [0 for i in range(top*top)]
        self.df_map = pd.DataFrame(np.reshape(fill, (top, top)))
        self.points_dict = {}
        self.points_list = []
        self.draw_lines()

    def birange(self, points, step):
        if points[0] < points[1]:
            return range(points[0], points[1]+1, step)
        else:
            return range(points[1], points[0]+1, step)

    def draw_line(self, line):
        if line[0][0] == line[1][0]:
            for i in self.birange([line[0][1], line[1][1]], 1):
                self.df_map.iloc[i, line[0][0]] += 1
        elif line[0][1] == line[1][1]:
            for i in self.birange([line[0][0], line[1][0]], 1):
                self.df_map.iloc[line[0][1], i] += 1

    def draw_line2(self, line):
        line_dict = {}
        print(line)
        if line[0][0] == line[1][0]:
            for i in self.birange([line[0][1], line[1][1]], 1):
                line_dict[line[0][0], i] = 1
        if line[0][1] == line[1][1]:
            for i in self.birange([line[0][0], line[1][0]], 1):
                line_dict[i, line[0][1]] = 1
        print(line_dict)
        # print(dict(Counter(line_dict) + Counter(line_dict)))
        print('=============================================')
        self.points_dict = dict(Counter(self.points_dict) + Counter(line_dict))
        print(self.points_dict)
        print('=============================================')

    def draw_line3(self, line):
        points_list = []
        print('=============================================')
        print(f'Plotting points for line: {line}')
        if line[0][0] == line[1][0]:
            for i in self.birange([line[0][1], line[1][1]], 1):
                points_list.append(str(f'{line[0][0]}, {i}'))
        elif line[0][1] == line[1][1]:
            for i in self.birange([line[0][0], line[1][0]], 1):
                points_list.append(str(f'{i}, {line[0][1]}'))

        print(f'New points added: {points_list}')
        self.points_list = self.points_list + points_list
        print('=============================================')
        print('.')

    def draw_lines(self):
        for line in self.line_list:
            self.draw_line3(line)

    def intersection_count(self):
        df = self.df_map.copy()
        df.replace({1: 0}, inplace=True)
        return df.any().sum()

    def intersection_count2(self):
        point_set = set(self.points_list)
        return len(self.points_list) - len(point_set)


if __name__ == "__main__":
    puzzle_input = Puzzle(year=2021, day=5).input_data

    puzzle_input = "\
0,9 -> 5,9\n\
8,0 -> 0,8\n\
9,4 -> 3,4\n\
2,2 -> 2,1\n\
7,0 -> 7,4\n\
6,4 -> 2,0\n\
0,9 -> 2,9\n\
3,4 -> 1,4\n\
0,0 -> 8,8\n\
5,5 -> 8,2"
    vents = Vent_Map(puzzle_input)
    print("Here's a map of the vents:")
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     pp.pprint(vents.df_map, depth=1000)
    pp.pprint(vents.points_list)
    print(f"There are {vents.intersection_count2()} intersections.")
