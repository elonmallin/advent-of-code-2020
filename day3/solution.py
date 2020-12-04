import os
import functools

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
lines = list(map(lambda l: list(l.replace('\n', '')), input_file)) # double array


def solve(lines, x, y, step_x, step_y, treeHitCount):
    if lines[y][x%len(lines[0])] == '#':
        treeHitCount += 1

    x += step_x
    y += step_y

    if y >= len(lines):
        return treeHitCount
    else:
        return solve(lines, x, y, step_x, step_y, treeHitCount)


print('Solution 1:', solve(lines, 0, 0, 3, 1, 0))

print('Solution 2:', functools.reduce(
    lambda a, b: a * b, 
    [
        solve(lines, 0, 0, 1, 1, 0),
        solve(lines, 0, 0, 3, 1, 0),
        solve(lines, 0, 0, 5, 1, 0),
        solve(lines, 0, 0, 7, 1, 0),
        solve(lines, 0, 0, 1, 2, 0)
    ]
))
