import os
import re
import functools
import random
import math

# input_file = open(os.path.join(os.path.dirname(__file__), './test_input.txt'))
input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
lines = list(map(lambda l: l.replace('\n', ''), input_file))


class Seat:
    def __init__(self, row, col, seat_id):
        self.row = row
        self.col = col
        self.seat_id = seat_id

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.__dict__)
    
    @staticmethod
    def create(line):
        row_count = 127
        col_count = 7
        seat = Seat(0, 0, 0)

        for c in line:
            if c == 'F':
                row_count = math.floor((row_count - seat.row) / 2) + seat.row
            elif c == 'B':
                seat.row = math.ceil((row_count - seat.row) / 2) + seat.row

            if c == 'L':
                col_count = math.floor((col_count - seat.col) / 2) + seat.col
            elif c == 'R':
                seat.col = math.ceil((col_count - seat.col) / 2) + seat.col

        seat.seat_id = (seat.row * 8) + seat.col

        return seat


def solve_part_1(lines):
    highest = 0

    for l in lines:
        tmp = Seat.create(l).seat_id
        if tmp > highest:
            highest = tmp

    return highest


def solve_part_2(lines):
    seats = []

    for l in lines:
        seats.append(Seat.create(l))

    seats.sort(key = lambda s: s.seat_id)

    prev = seats[0]
    for i, seat in enumerate(seats[1:-1]):
        if seat.seat_id - 1 != prev.seat_id or seat.seat_id + 1 != seats[i+2].seat_id:
            return seat.seat_id + 1

        prev = seat

    return -1


print('Highest seat id:', solve_part_1(lines))
print('My seat id:', solve_part_2(lines))
