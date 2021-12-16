from aocd.models import Puzzle
# https://pypi.org/project/advent-of-code-data/

if __name__ == "__main__":
    input = Puzzle(2021, 6).input_data
    ages = input.split(',')
    ages = list(map(int, ages))
    ages = [age+1 for age in ages]

    fishes = [0 for f in range(9)]
    for a in ages:
        fishes[a] += 1

    for idx, fish in enumerate(fishes):
        print(f'{idx}:{fish}')
    print(f" There are {sum(fishes)} little fishies to start.")

    for i in range(257):
        new_fishes = [0 for f in range(9)]
        for idx, f in enumerate(fishes):
            if idx < 1:
                new_fishes[8] += f
                new_fishes[6] += f
            else:
                new_fishes[idx-1] += f
        fishes = new_fishes.copy()

    print(f" There are now {sum(fishes)} little fishies.")
