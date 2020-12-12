import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: int(l), all_text.split('\n')))


class part_1:
    @staticmethod
    def solve(lines, pre_len):
        for i, l in enumerate(lines[pre_len:]):
            if not part_1.brute_force_check(lines, i+pre_len, pre_len, l):
                return l

        return False


    @staticmethod
    def brute_force_check(lines, idx, pre_len, n_check):
        for i in range(idx-pre_len, idx):
            for j in range(idx-pre_len, idx):
                if i == j:
                    continue

                if lines[i] + lines[j] == n_check:
                    return True

        return False


class part_2:
    @staticmethod
    def solve(lines, match):
        for i, l in enumerate(lines):
            (ok, n_min, n_max) = part_2.brute_force_check(lines, i, match)
            if ok:
                return n_min + n_max

        return False


    @staticmethod
    def brute_force_check(lines, idx, n_check):
        n_sum = 0
        n_min = lines[idx]
        n_max = lines[idx]

        for l in lines[idx:]:
            n_min = min(n_min, l)
            n_max = max(n_max, l)
            n_sum += l

            if n_sum > n_check:
                return (False, 0, 0)
            elif n_sum == n_check:
                return (True, n_min, n_max)

        return (False, 0, 0)


print('Solution part 1:', part_1.solve(lines, 25))
print('Solution part 2:', part_2.solve(lines, 32321523))