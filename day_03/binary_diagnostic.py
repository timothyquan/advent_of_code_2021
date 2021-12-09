import pandas as pd
import pprint as pp

from aocd.models import Puzzle


# set up puzzle from aocd
# https://pypi.org/project/advent-of-code-data/
puzzle_input = Puzzle(year=2021, day=3).input_data
input = [i for i in puzzle_input.split('\n')]

# part 1: ---------------------------------------------------------


def binarylist_to_decimal(bitlist):
    pwr = 0
    dec = 0
    for i in range(len(bitlist)-1, -1, -1):
        dec += int(bitlist[i]) * pow(2, pwr)
        pwr += 1
    return dec


bit_list = []
for i in input:
    bit_list.append([c for c in i])
df = pd.DataFrame(bit_list)

gammalist = [int(c) for c in (df.mode().values.tolist()[0])]
# invert the bits in gammalist to get epsilonlist
epsilonlist = [(int(c) - 1) * -1 for c in gammalist]

print(
    f'The gamma rate is {binarylist_to_decimal(gammalist)} and the epsilon rate is {binarylist_to_decimal(epsilonlist)}.')
print(
    f'The power consumption of the submarine is {binarylist_to_decimal(gammalist) * binarylist_to_decimal(epsilonlist)}.')


# part 2: ---------------------------------------------------------

def rating(df_bit, seektype, iter=0):
    '''Seektype 1: oxygen gerator rating, 0: CO2 scrubber rating'''

    one_count = df_bit[iter].value_counts()['1']
    zero_count = df_bit[iter].value_counts()['0']
    if one_count == zero_count:
        seek = seektype
    elif seektype == 0:
        seek = int(one_count < zero_count)
    else:
        seek = int(one_count > zero_count)

    seek = str(seek)

    new_df = df_bit[df_bit[iter] == seek]
    if len(new_df) < 2:
        return new_df

    return rating(new_df.reset_index(drop=True), seektype, iter=iter+1)


oxygen_gen_rating = binarylist_to_decimal(
    rating(df, 1).values.tolist()[0])
co2_scrubber_rating = binarylist_to_decimal(
    rating(df, 0).values.tolist()[0])


print(
    f'The oxygen generator rating is {oxygen_gen_rating}, the co2 scrubber rating is {co2_scrubber_rating}.')
print(
    f'The life support rating (oxygen generator rating * co2 scrubber rating) is {oxygen_gen_rating*co2_scrubber_rating}.')
