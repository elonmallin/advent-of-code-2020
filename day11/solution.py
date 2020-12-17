import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: l, all_text.split('\n')))


class part_1:
    @staticmethod
    def solve(lines):
        curr_state = ''.join(lines)

        while True:
            lines_cpy = lines.copy()

            for y in range(len(lines)):
                for x in range(len(lines[y])):
                    part_1.apply_rules(lines, lines_cpy, x, y)

            next_state = ''.join(lines)
            if next_state == curr_state:
                curr_state = next_state
                break
            else:
                curr_state = next_state

        return len(re.findall('#', curr_state))
            

    @staticmethod
    def apply_rules(lines, lines_cpy, x, y):
        if lines_cpy[y][x] == 'L' and part_1.count_adjacent_occupied(lines_cpy, x, y) == 0:
            lines[y] = lines[y][:x] + '#' + lines[y][x+1:]
        elif lines_cpy[y][x] == '#' and part_1.count_adjacent_occupied(lines_cpy, x, y) >= 4:
            lines[y] = lines[y][:x] + 'L' + lines[y][x+1:]


    @staticmethod
    def count_adjacent_occupied(lines, x, y):
        count = 0

        # Line above
        count += 1 if part_1.get_position(lines, x-1, y-1) == '#' else 0
        count += 1 if part_1.get_position(lines, x, y-1) == '#' else 0
        count += 1 if part_1.get_position(lines, x+1, y-1) == '#' else 0

        # Same line
        count += 1 if part_1.get_position(lines, x-1, y) == '#' else 0
        count += 1 if part_1.get_position(lines, x+1, y) == '#' else 0

        # Line below
        count += 1 if part_1.get_position(lines, x-1, y+1) == '#' else 0
        count += 1 if part_1.get_position(lines, x, y+1) == '#' else 0
        count += 1 if part_1.get_position(lines, x+1, y+1) == '#' else 0

        return count


    @staticmethod
    def get_position(lines, x, y):
        if 0 <= y and y < len(lines) and 0 <= x and x < len(lines[y]):
            return lines[y][x]

        return None


class part_2:
    @staticmethod
    def solve(lines):
        curr_state = ''.join(lines)

        while True:
            lines_cpy = lines.copy()

            for y in range(len(lines)):
                for x in range(len(lines[y])):
                    part_2.apply_rules(lines, lines_cpy, x, y)

            next_state = ''.join(lines)
            if next_state == curr_state:
                curr_state = next_state
                break
            else:
                curr_state = next_state

        return len(re.findall('#', curr_state))
            

    @staticmethod
    def apply_rules(lines, lines_cpy, x, y):
        if lines_cpy[y][x] == 'L' and part_2.count_vector_occupied(lines_cpy, x, y) == 0:
            lines[y] = lines[y][:x] + '#' + lines[y][x+1:]
        elif lines_cpy[y][x] == '#' and part_2.count_vector_occupied(lines_cpy, x, y) >= 5:
            lines[y] = lines[y][:x] + 'L' + lines[y][x+1:]


    @staticmethod
    def count_vector_occupied(lines, x, y):
        count = 0

        # Vec up \ | /
        count += 1 if part_2.get_collission(lines, x, y, -1, -1) else 0
        count += 1 if part_2.get_collission(lines, x, y, 0, -1) else 0
        count += 1 if part_2.get_collission(lines, x, y, 1, -1) else 0

        # Vec left and right - -
        count += 1 if part_2.get_collission(lines, x, y, -1, 0) else 0
        count += 1 if part_2.get_collission(lines, x, y, 1, 0) else 0

        # Vec down / | \
        count += 1 if part_2.get_collission(lines, x, y, -1, 1) else 0
        count += 1 if part_2.get_collission(lines, x, y, 0, 1) else 0
        count += 1 if part_2.get_collission(lines, x, y, 1, 1) else 0

        return count


    @staticmethod
    def get_position(lines, x, y):
        if 0 <= y and y < len(lines) and 0 <= x and x < len(lines[y]):
            return lines[y][x]

        return None

    @staticmethod
    def get_collission(lines, x, y, vec_x, vec_y):
        while True:
            x += vec_x
            y += vec_y
            c = part_2.get_position(lines, x, y)
            if c in [None, 'L']:
                return False
            elif c == '#':
                return True


print('Solution part 1:', part_1.solve(lines))
print('Solution part 2:', part_2.solve(lines))
