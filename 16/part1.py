filename = "input.txt"


with open(filename) as f:
    lines = f.readlines()

map = []
for l in lines:
    l = l.strip()
    if len(l) < 3:
        continue

    one_row = [x for x in l]
    map.append(one_row)


def move_beam(one_beam, map):
    (row, col, direction) = one_beam

    ret = []
    if map[row][col] == ".":
        if direction == "r":
            ret.append((row, col+1, direction))
        elif direction == "l":
            ret.append((row, col-1, direction))
        elif direction == "u":
            ret.append((row-1, col, direction))
        elif direction == "d":
            ret.append((row+1, col, direction))
    elif map[row][col] == "/":
        if direction == "r":
            ret.append((row-1, col, 'u'))
        elif direction == "l":
            ret.append((row+1, col, 'd'))
        elif direction == "u":
            ret.append((row, col+1, 'r'))
        elif direction == "d":
            ret.append((row, col-1, 'l'))
    elif map[row][col] == '\\': # escape the \
        if direction == "r":
            ret.append((row+1, col, 'd'))
        elif direction == "l":
            ret.append((row-1, col, 'u'))
        elif direction == "u":
            ret.append((row, col-1, 'l'))
        elif direction == "d":
            ret.append((row, col+1, 'r'))
    elif map[row][col] == "|":
        if direction == "r" or direction == "l":
            ret.append((row-1, col, 'u'))
            ret.append((row+1, col, 'd'))
        elif direction == "u":
            ret.append((row-1, col, 'u'))
        elif direction == "d":
            ret.append((row+1, col, 'd'))
    elif map[row][col] == "-":
        if direction == "u" or direction == "d":
            ret.append((row, col-1, 'l'))
            ret.append((row, col+1, 'r'))
        elif direction == "r":
            ret.append((row, col+1, 'r'))
        elif direction == "l":
            ret.append((row, col-1, 'l'))

    max_h = len(map)
    max_w = len(map[0])
    ret_final = []
    for b in ret:
        (row, col, _) = b
        if row < 0 or col < 0:
            continue
        if row >= max_h or col >= max_w:
            continue
        ret_final.append(b)
    return ret_final

def print_energized(tiles_energized, map):
    for row in range(len(map)):
        print("")
        for col in range(len(map[0])):
            if (row, col) in tiles_energized:
                print("#", end='')
            else:
                print(f"{map[row][col]}", end='')
    
tiles_energized = set()
beams = [(0,0,"r")]
seen = set()
seen.add((0,0,"r"))
tiles_energized.add((0,0))
while len(beams):
    one_beam = beams.pop(0)

    beam_res = move_beam(one_beam, map)
    
    for b in beam_res:
        if b in seen:
            continue
        seen.add(b)

        (row, col, _) = b
        tiles_energized.add((row,col))
        
        beams.append(b)

print_energized(tiles_energized, map)
print(f"Energized {len(tiles_energized)}")
