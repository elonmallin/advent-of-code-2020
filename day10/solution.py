import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_short_input.txt'))
# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: int(l), all_text.split('\n')))


class part_1:
    def solve(lines):
        lines = sorted(lines)
        joltDiffs = [0,0,0]

        lastJolt = 0
        for jolt in lines:
            diff = jolt - lastJolt
            joltDiffs[diff - 1] += 1

            lastJolt = jolt

        joltDiffs[2] += 1

        return (joltDiffs, joltDiffs[0] * joltDiffs[2])


class part_2:
    def solve(lines):
        lines = sorted(lines)
        lines.insert(0, 0)
        cache = {}

        num_ways = part_2.solve_recurse(lines, 0, cache)

        return num_ways


    def solve_recurse(lines, idx, cache):
        if idx >= len(lines) - 1:
            return 1

        num_ways = 0

        for i in range(1, 4):
            if idx + i >= len(lines):
                break

            diff = lines[idx + i] - lines[idx]
            if diff <= 3:
                if idx + i in cache:
                    num_ways += cache[idx + i]
                else:
                    num_ways += part_2.solve_recurse(lines, idx + i, cache)

        cache[idx] = num_ways

        return num_ways


# print('Solution part 1:', part_1.solve(lines))
print('Solution part 2:', part_2.solve(lines))
