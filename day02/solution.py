import os
import re
import functools

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
lines = list(map(lambda l: l.replace('\n', ''), input_file))

def is_policy_ok(s):
    min, max, letter, pw = re.findall('(\d+)-(\d+) (\w+): (\w+)', s)[0]
    count = len(re.split(letter, pw)) - 1

    return count in range(int(min), int(max)+1)


def is_policy_ok_part_2(s):
    p1, p2, l, pw = re.findall('(\d+)-(\d+) (\w+): (\w+)', s)[0]
    p1, p2 = int(p1)-1, int(p2)-1

    return pw[p1] != pw[p2] and (pw[p1] == l or pw[p2] == l)


def solve(lines, policy_ok_check):
    valid_count = 0

    for line in lines:
        if policy_ok_check(line):
            valid_count += 1

    return valid_count


print('Solution 1:', solve(lines, is_policy_ok))
print('Solution 2:', solve(lines, is_policy_ok_part_2))
