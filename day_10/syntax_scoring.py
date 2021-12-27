from aocd.models import Puzzle


class Line:
    def __init__(self, line):
        self.line = list(line)
        self.chunks = []
        pass

    def find_errors(self):
        opener = False
        openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
        closers = {')': '(', ']': '[', '}': '{', '>': '<'}
        err_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

        print('')
        print(f"Line: {''.join(self.line)}", end='')
        for c in self.line:
            if c in openers:
                self.chunks.append(c)
            elif c in closers.keys():
                if not closers[c] == self.chunks[-1]:
                    print(
                        f":-=-=-=-=-=-=-=-=-=-=-=- Expected {openers[self.chunks[-1]]} but found {c} instead. ")
                    return err_map[c]
                else:
                    self.chunks.pop(-1)
        print(":-=-=-=-=-=-=-=-=-=-=-=- No errors detected!")
        return 0

    def find_closure(self):
        score = 0
        closers = []
        points = {'(': 1, '[': 2, '{': 3, '<': 4}

        for c in reversed(self.chunks):
            score = (score * 5) + points[c]
        return score


if __name__ == "__main__":
    with open('./day_10/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 10).input_data

    errsum = 0
    line_list = []
    for l in lines.split('\n'):
        line_list.append(Line(l))
        err = line_list[-1].find_errors()
        errsum += err
        if err:
            line_list.pop(-1)

    print(f"The sum of all first errors is: {errsum}.")

    closcores = []
    for l in line_list:
        closcore = l.find_closure()
        closcores.append(closcore)
        print(f"{''.join(l.line)} found closure with a score of : {closcore}")

    mid_score = sorted(closcores)[int(len(closcores)/2)]
    print(f"The middle score is {mid_score}.")
