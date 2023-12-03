import re
import numpy as np

# Main data structure
# A dict of (row, column) -> full number that the coordinate is part of
# So there for a 3 digit number there will be three (row, column) -> 123
data = {}

row_max = 140
col_max = 140
filename = "input.txt"

def add_list(data, accumulated_positions, accumulated_number:int):
    for p in accumulated_positions:
        data[p] = accumulated_number

def check_match(row, col):
    ret = 0
    if (row, col) in data:
        ret = data[(row, col)]

        # now delete this value everywhere so we don't double count
        # the full number can only exist horizontally
        del data[(row, col)]

        col_right = col+1
        while col_right < col_max and (row, col_right) in data:
            del data[(row, col_right)]
            col_right += 1

        col_left = col-1
        while col_left >= col_max and (row, col_left) in data:
            del data[(row, col_left)]
            col_left -= 1
            
    return ret

numbers = set([str(x) for x in range(10)])


with open(filename) as f:
    lines = f.readlines()



# a list of tuples of special characters (char, row, column)
special_chars = []

# a list of row, column tuples for adjacent digits forming one number
accumulated_positions = None
accumulated_number = None

# Build dataset
for row, l in enumerate(lines):
    l = l.strip()
    if len(l) < 2:
        continue

    for column, v in enumerate(l):
        if v in numbers:
            if accumulated_positions is None:
                accumulated_positions = [(row, column)]
                accumulated_number = v
            else:
                accumulated_positions.append((row, column))
                accumulated_number += v
        else: # special char or . reset number
            if accumulated_positions is not None:
                add_list(data, accumulated_positions, int(accumulated_number))
            accumulated_positions = None
            accumulated_number = None
            
            if v != ".":
                special_chars.append((v, row, column))

    # New row, reset number as well
    if accumulated_positions is not None:
        add_list(data, accumulated_positions, int(accumulated_number))
    accumulated_positions = None
    accumulated_number = None

# Now for each special char see what is adjacent to it

sum = 0
for (_, s_row, s_col) in special_chars:
    for row_add in [-1, 0, 1]:
        for col_add in [-1, 0, 1]:

            if 0 <= s_row + row_add < row_max and 0<= s_col + col_add < col_max:
                sum += check_match(s_row+row_add, s_col+col_add)

print(f"Not counted {data}")
print(f"Sum is {sum}")

