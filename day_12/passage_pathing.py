from collections import defaultdict
from aocd.models import Puzzle


class Cave_System:
    def __init__(self, input):
        input = input.splitlines()
        input = [l.split('-') for l in input]
        self.caves = defaultdict()

        for l in input:
            for c in l:
                self.caves[c] = set()

        for l in input:
            self.caves[l[0]].add(l[1])
            self.caves[l[1]].add(l[0])

        self.visited = set()
        self.paths = []

    def find_paths(self, path: list = ['start'], visited: set = set(), cave: str = 'start'):
        if cave == 'end':
            self.paths.append(path)
        else:
            if cave.islower():
                visited.add(cave)
            for next_cave in self.caves[cave]:
                if next_cave not in visited:
                    self.find_paths(path+[next_cave], set(visited), next_cave)


if __name__ == "__main__":
    with open('./day_12/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 12).input_data

    caves = Cave_System(lines)
    caves.find_paths()
    print(f"There are {len(caves.paths)} paths through the cave system.")
