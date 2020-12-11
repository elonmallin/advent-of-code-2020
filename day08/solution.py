import os
import re

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

all_text = input_file.read().strip('\n')
lines = list(map(lambda l: l, all_text.split('\n')))


class part_1:
    @staticmethod
    def solve(lines):
        visited = [False] * len(lines)
        acc = 0

        i = 0
        while True:
            if visited[i]:
                break

            visited[i] = True
            l = lines[i]

            (instruction, n) = re.findall('^(\w+) ([+-]\d+)', l)[0]
            n = int(n)

            if instruction == 'nop':
                i += 1
            elif instruction == 'acc':
                i += 1
                acc += n
            elif instruction == 'jmp':
                i += n

        return acc


class part_2:
    @staticmethod
    def solve(lines, visited, acc, i, can_override):
        finished = False

        while True:
            if i == len(lines):
                finished = True
                break
            elif visited[i] or i > len(lines) or i < 0:
                break

            visited[i] = True
            l = lines[i]

            (instruction, n) = re.findall('^(\w+) ([+-]\d+)', l)[0]
            n = int(n)

            if instruction == 'nop':
                if can_override:
                    (inner_finished, inned_acc) = part_2.solve(lines, visited.copy(), acc, i + n, False)
                    if inner_finished:
                        return (inner_finished, inned_acc)
                i += 1
            elif instruction == 'jmp':
                if can_override:
                    (inner_finished, inned_acc) = part_2.solve(lines, visited.copy(), acc, i + 1, False)
                    if inner_finished:
                        return (inner_finished, inned_acc)
                i += n
            elif instruction == 'acc':
                i += 1
                acc += n

        return (finished, acc)


print('Solution part 1:', part_1.solve(lines))
print('Solution part 2:', part_2.solve(lines, [False] * len(lines), 0, 0, True))
