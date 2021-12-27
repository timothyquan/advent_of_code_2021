from aocd.models import Puzzle


class Line:
    def __init__(self, line):
        self.line = list(line)
        pass

    def find_errors(self):
        opener = False
        openers = {'(': ')', '[': ']', '{': '}', '<': '>'}
        closers = {')': '(', ']': '[', '}': '{', '>': '<'}
        err_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
        chunks = []
        print('')
        print(f"Line: {''.join(self.line)}", end='')
        for c in self.line:
            if c in openers:
                chunks.append(c)
            elif c in closers.keys():
                if not closers[c] == chunks[-1]:
                    print(
                        f":-=-=-=-=-=-=-=-=-=-=-=- Expected {openers[chunks[-1]]} but found {c} instead. ")
                    return err_map[c]
                else:
                    chunks.pop(-1)
        print(":-=-=-=-=-=-=-=-=-=-=-=- No errors detected!")
        return 0


if __name__ == "__main__":
    with open('./day_10/sample_input.txt') as f:
        lines = f.read()
    lines = Puzzle(2021, 10).input_data

    errsum = 0
    for l in lines.split('\n'):
        errsum += Line(l).find_errors()

    print(errsum)
