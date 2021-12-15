from aocd.models import Puzzle
# https://pypi.org/project/advent-of-code-data/


class Fish_School:
    def __init__(self):
        self.fishes = []
        pass

    def add_fish(self, fish):
        self.fishes.append(fish)

    def print(self):
        fish_list = []
        for idx, f in enumerate(self.fishes):
            fish_list.append(f.age)
        print(fish_list)

    def age_day(self):
        for fish in self.fishes:
            fish.age_day()


class Lantern_Fish:
    def __init__(self, school, age=9):
        self.age = age
        self.school = school
        pass

    def age_day(self):
        self.age -= 1
        if self.age < 0:
            self.school.add_fish(Lantern_Fish(self.school))
            self.age = 6


if __name__ == "__main__":
    input = '3,4,3,1,2'
    #input = Puzzle(2021, 6).input_data
    ages = input.split(',')
    ages = list(map(int, ages))
    school = Fish_School()
    for a in ages:
        school.add_fish(Lantern_Fish(school, age=a))

    for i in range(80):
        # print(f"Day: {i}")
        # school.print()
        school.age_day()

    print(f'There are now {len(school.fishes)} little fishies. ')
    pass
