from aocd.models import Puzzle
# https://pypi.org/project/advent-of-code-data/

from collections import Counter


class Vent_Map:
    def __init__(self, input_string):
        line_list = input_string.replace(
            ' -> ', ',', ).replace('\n', ',').split(',')
        line_list = list(map(int, line_list))
        line_list = [line_list[i:i+2] for i in range(0, len(line_list), 2)]
        line_list = [line_list[i:i+2] for i in range(0, len(line_list), 2)]

        self.line_list = line_list
        self.point_list = []
        self.line_test = input_string.split('\n')
        self.draw_lines()

    def birange(self, points, step):
        '''Like range but bidirectional'''
        '''Points = list of integers'''
        if points[0] < points[1]:
            return range(points[0], points[1]+1, step)
        else:
            return range(points[0], points[1]-1, -1 * step)

    def draw_line(self, line):
        point_list = []
        if line[0][0] == line[1][0]:
            for i in self.birange([line[0][1], line[1][1]], 1):
                point_list.append((line[0][0], i))
        elif line[0][1] == line[1][1]:
            for i in self.birange([line[0][0], line[1][0]], 1):
                point_list.append((i, line[0][1]))
        else:
            xrange = [i for i in self.birange([line[0][0], line[1][0]], 1)]
            yrange = [i for i in self.birange([line[0][1], line[1][1]], 1)]
            for i, r in enumerate(xrange):
                point_list.append((xrange[i], yrange[i]))
        self.point_list = self.point_list + point_list

    def draw_lines(self):
        for line in self.line_list:
            self.draw_line(line)

    def intersection_count(self):
        point_set = set(self.point_list)
        dict_count = {}
        for p in self.point_list:
            try:
                dict_count[p] += 1
            except:
                dict_count[p] = 1
        intersection_count = 0
        for v in dict_count.values():
            if v > 1:
                intersection_count += 1

        return intersection_count


if __name__ == "__main__":
    puzzle_input = Puzzle(year=2021, day=5).input_data
    vents = Vent_Map(puzzle_input)
    print(f"There are {vents.intersection_count()} intersections.")
