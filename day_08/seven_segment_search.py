from aocd.models import Puzzle
import pprint as pp


class Entry:
    def __init__(self, vals):
        self.sig_pats = vals[0]
        self.out_vals = vals[1]
        self.count1478 = 0
        self.decoder = {}
        self.encoder = {}

    def detect_known_nums(self, vals_list):
        '''Identifies 1, 4, 7, 8 by the known character count'''
        nums = [2, 4, 3, 7]
        for s in vals_list:
            if len(s) in nums:
                self.count1478 += 1
            if len(s) == 2:
                self.decoder[s] = 1
                self.encoder[1] = s
            elif len(s) == 3:
                self.decoder[s] = 7
                self.encoder[7] = s
            elif len(s) == 4:
                self.decoder[s] = 4
                self.encoder[4] = s
            elif len(s) == 7:
                self.decoder[s] = 8
                self.encoder[8] = s

    def detect_by_subset(self, vals_list):
        # 6 : 0, 6, 9
        # 5 : 2, 3, 5
        bdset = set(self.encoder[4]) - set(self.encoder[1])
        for s in vals_list:
            if len(s) == 6:
                if set(self.encoder[4]).issubset(s):
                    self.decoder[s] = 9
                    self.encoder[9] = s
                elif set(self.encoder[1]).issubset(s):
                    self.decoder[s] = 0
                    self.encoder[0] = s
                else:
                    self.decoder[s] = 6
                    self.encoder[6] = s
            elif len(s) == 5:
                if set(self.encoder[7]).issubset(s):
                    self.decoder[s] = 3
                    self.encoder[3] = s
                elif bdset.issubset(s):
                    self.decoder[s] = 5
                    self.encoder[5] = s
                else:
                    self.decoder[s] = 2
                    self.encoder[2] = s

    def detect_in_out(self):
        self.detect_known_nums(self.out_vals)
        self.detect_by_subset(self.out_vals)

    def detect_in_sig(self):
        self.detect_known_nums(self.sig_pats)
        self.detect_by_subset(self.sig_pats)

    def decode_string(self, string):
        for s in self.decoder:
            if set(string) == set(s):
                return s

    def decode_output(self):
        outstr = ''
        for o in self.out_vals:
            outstr += str(self.decoder[self.decode_string(o)])
        return outstr


def parse_input(input_string):
    input = input_string.split('\n')
    input = [l.split(' | ') for l in input]
    input = [[c.split(' ') for c in l] for l in input]
    return input
    pass


if __name__ == '__main__':

    # with open('./day_08/sample_input.txt') as f:
    #     lines = f.read()
    lines = Puzzle(2021, 8).input_data
    input = parse_input(lines)
    ents = []
    for i in input:
        ents.append(Entry(i))

    count = 0
    for e in ents:
        e.detect_known_nums(e.out_vals)
        count += e.count1478

    print(f'1, 4, 7, 8 appear {count} times in output. ')

    out_total = 0
    for e in ents:
        e.detect_in_sig()
        e.detect_in_out()
        out_total += int(e.decode_output())
    print(f"The total of all output values is {out_total}")
