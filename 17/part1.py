#!/usr/bin/python3

import math
import numpy as np
import re
from collections import defaultdict
import sys
np.set_printoptions(threshold=sys.maxsize)

# defaultdict(str)
# defaultdict(int)

data = []


with open("input2.txt") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data.append(v)


width = len(data[0])
height = len(data)

graph = np.zeros((height, width), np.uint32)

memoize = np.zeros((height, width), np.uint32)
for i in range(width):
    for j in range(height):
        graph[j][i] = data[j][i]
        memoize[j][i] = 4294967295


paths = []
# ([(row, col), (row, col)], heat_loss, direction, consecutive)
paths.append(([(0,0)], 0, None, 0))

#print(f"{graph}")


def direction_valid(new_direction, last_direction, consecutive):
    # can't go more than 3 in a row
    if consecutive == 3 and new_direction == last_direction:
        return False

    # can't reverse
    if new_direction == "r" and last_direction == "l":
        return False
    if new_direction == "l" and last_direction == "r":
        return False
    if new_direction == "u" and last_direction == "d":
        return False
    if new_direction == "d" and last_direction == "u":
        return False

    return True
    
while len(paths):
    (route, heat_loss, last_direction, consecutive) = paths.pop(0)
    (x, y) = route[-1]

    if y == 0 and x == 4:
        print(f"route is {route}")
    # try going left 
    if x > 0 and direction_valid("l", last_direction, consecutive):
        new_heat_loss = heat_loss + graph[y][x-1]
        if new_heat_loss < memoize[y][x-1] and (x-1, y) not in route:
            memoize[y][x-1] = new_heat_loss
            new_route = route.copy()
            new_route.append((x-1, y))

            new_direction = "l"
            if last_direction == "l":
                new_consecutive = consecutive + 1
            else:
                new_consecutive = 1
            paths.append((new_route, new_heat_loss, new_direction, new_consecutive))

    # try going right
    if x < width-1 and direction_valid("r", last_direction, consecutive):
        new_heat_loss = heat_loss + graph[y][x+1]
        if new_heat_loss < memoize[y][x+1] and (x+1, y) not in route:
            memoize[y][x+1] = new_heat_loss
            new_route = route.copy()
            new_route.append((x+1, y))

            new_direction = "r"
            if last_direction == "r":
                new_consecutive = consecutive + 1
            else:
                new_consecutive = 1
            paths.append((new_route, new_heat_loss, new_direction, new_consecutive))

    # try going up
    if y > 0 and direction_valid("u", last_direction, consecutive):
        new_heat_loss = heat_loss + graph[y-1][x]
        if new_heat_loss < memoize[y-1][x] and (x, y-1) not in route:
            memoize[y-1][x] = new_heat_loss
            new_route = route.copy()
            new_route.append((x, y-1))

            new_direction = "u"
            if last_direction == "u":
                new_consecutive = consecutive + 1
            else:
                new_consecutive = 1
            paths.append((new_route, new_heat_loss, new_direction, new_consecutive))

    # try going down
    if y < height -1 and direction_valid("d", last_direction, consecutive):
        new_heat_loss = heat_loss + graph[y+1][x]
        if new_heat_loss < memoize[y+1][x] and (x, y+1) not in route:
            memoize[y+1][x] = new_heat_loss
            new_route = route.copy()
            new_route.append((x, y+1))

            new_direction = "d"
            if last_direction == "d":
                new_consecutive = consecutive + 1
            else:
                new_consecutive = 1
            paths.append((new_route, new_heat_loss, new_direction, new_consecutive))

memoize[0][0] = 0
print(f"{memoize}")
print(f"Final: {memoize[-1][-1]}")


    
            
        


