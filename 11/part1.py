import itertools

filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

def compute_distance(a, b):
    (a_y, a_x) = a
    (b_y, b_x) = b

    return  abs(a_x-b_x) + abs(a_y-b_y)

# input data is 140x140

# list of (y, x) coordinates of galaxies
galaxies = []

rows_occupied = [0] * 140
cols_occupied = [0] * 140
for i, l in enumerate(lines):
    l = l.strip()
    if len(l)<3:
        continue

    
    for j, v in enumerate(l):
        if v == "#":
            galaxies.append((i, j))
            rows_occupied[i] += 1
            cols_occupied[j] += 1


print("empty rows")
empty_rows = []
for i, r in enumerate(rows_occupied):
    if r == 0:
        print(f"{i}")
        empty_rows.append(i)

print("empty cols")
empty_cols = []
for i, c in enumerate(cols_occupied):
    if c == 0:
        print(f"{i}")
        empty_cols.append(i)

new_galaxies = []
for (g_y, g_x) in galaxies:

    preceeding_empty_rows = 0
    for e in empty_rows:
        if e < g_y:
            preceeding_empty_rows += 1

    preceeding_empty_cols = 0
    for e in empty_cols:
        if e < g_x:
            preceeding_empty_cols += 1

    new_galaxies.append((g_y + preceeding_empty_rows, g_x + preceeding_empty_cols))


galaxy_pairs = list(itertools.combinations(new_galaxies, 2))
#print(f"{len(galaxy_pairs)} pairs for {len(new_galaxies)}")
sum = 0
for (p1, p2) in galaxy_pairs:
    sum += compute_distance(p1, p2)

print(f"{sum}")
            
    
