import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines_part_1 = list(map(lambda l: l.replace('\n', ''), all_text.split('\n\n')))
lines_part_2 = list(map(lambda l: { 'line': l.replace('\n', ''), 'people_count': len(l.split('\n')) }, all_text.split('\n\n')))


def solve_part_1(lines):
    count = 0

    for l in lines:
        hashmap = {}
        for c in l:
            if c not in hashmap:
                hashmap[c] = c
                count += 1

    return count


def solve_part_2(lines):
    count = 0

    for ll in lines:
        hashmap = {}

        for c in ll['line']:

            if c not in hashmap:
                hashmap[c] = True

                occurances_of_c = len(re.findall(c, ll['line']))
                if  occurances_of_c == ll['people_count']:
                    count += 1

    return count


print('Solution part 1:', solve_part_1(lines_part_1))
print('Solution part 2:', solve_part_2(lines_part_2))
