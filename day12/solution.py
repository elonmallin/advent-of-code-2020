import os
import re
import math

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: l, all_text.split('\n')))


def rotate(vec, deg):
    (x, y) = vec
    rad = math.radians(deg)
    x2 = x * math.cos(rad) - y * math.sin(rad)
    y2 = x * math.sin(rad) + y * math.cos(rad)

    return (round(x2), round(y2))


def move(pos, vec, dist):
    return (pos[0] + vec[0] * dist, pos[1] + vec[1] * dist)


class part_1:
    def solve(lines):
        move_vec = (1, 0)
        pos = (0, 0)

        for l in lines:
            (d, c) = re.findall('(\w)(\d+)', l)[0]
            c = int(c)

            if d in ['R', 'L']:
                move_vec = rotate(move_vec, c if d == 'L' else 360 - c)
            elif d == 'F':
                pos = move(pos, move_vec, c)
            elif d == 'N':
                pos = move(pos, (0, 1), c)
            elif d == 'E':
                pos = move(pos, (1, 0), c)
            elif d == 'S':
                pos = move(pos, (0, -1), c)
            elif d == 'W':
                pos = move(pos, (-1, 0), c)

        return abs(pos[0]) + abs(pos[1])


class part_2:
    def solve(lines):
        move_vec = (10, 1)
        pos = (0, 0)

        for l in lines:
            (d, c) = re.findall('(\w)(\d+)', l)[0]
            c = int(c)

            if d in ['R', 'L']:
                move_vec = rotate(move_vec, c if d == 'L' else 360 - c)
            elif d == 'F':
                pos = move(pos, move_vec, c)
            elif d == 'N':
                move_vec = move(move_vec, (0, 1), c)
            elif d == 'E':
                move_vec = move(move_vec, (1, 0), c)
            elif d == 'S':
                move_vec = move(move_vec, (0, -1), c)
            elif d == 'W':
                move_vec = move(move_vec, (-1, 0), c)

        return abs(pos[0]) + abs(pos[1])


print('Soution part 1:', part_1.solve(lines))
print('Soution part 2:', part_2.solve(lines))
