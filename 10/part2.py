# This is a gross solution but the only thing I could come up with. I didn't get any help or use a hint or anything so there's that.
# The solution is to take the map from part 1 and blow each tile up into a 3x3 tile so we can articulate the inside and outside surfaces
# even in areas between touching pipes in the 1x1 tile size. I didn't bother doing anything sneaky  so I just hard coded the mapping.


filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

data = [] # y, then x

seen_points = set()
for i, l in enumerate(lines):
    l = l.strip()
    if len(l)<3:
        continue

    data.append(l)

    if "S" in l:
        start_y = i
        start_x = l.index("S")



print(f"Start point {start_x} {start_y}")
seen_points.add((start_y, start_x))

#looking at the data, the S tile is a vertical pipe so we'll start looking up and down

start_points = [(start_y+1, start_x), (start_y-1, start_x)] # for main input, |
#start_points = [(start_y+1, start_x), (start_y, start_x+1)] # for test input, F
distance = 1
while start_points[0] != start_points[1]:
    #print(f"points are {start_points} at distance {distance} seen {seen_points}")
    new_start_points = []
    for s in start_points:
        seen_points.add(s)
        (start_y, start_x) = s

        point_type = data[start_y][start_x]

        if point_type == "|":
            new_start_points.append((start_y+1, start_x))
            new_start_points.append((start_y-1, start_x))

        elif point_type == "-":
            new_start_points.append((start_y, start_x+1))
            new_start_points.append((start_y, start_x-1))

        elif point_type == "L":
            new_start_points.append((start_y-1, start_x))
            new_start_points.append((start_y, start_x+1))

        elif point_type == "J":
            new_start_points.append((start_y-1, start_x))
            new_start_points.append((start_y, start_x-1))

        elif point_type == "7":
            new_start_points.append((start_y+1, start_x))
            new_start_points.append((start_y, start_x-1))

        elif point_type == "F":
            new_start_points.append((start_y+1, start_x))
            new_start_points.append((start_y, start_x+1))

        elif point_type == "S":
            continue
        else:
            print(f"ERROR at {s}")
            break

    new_start_points_filtered = []
    for n in new_start_points:
        if n in seen_points:
            continue
        new_start_points_filtered.append(n)

    distance += 1
    start_points = new_start_points_filtered

# add the terminus to the loop
seen_points.add(start_points[0])
# seen_points has everything in the pipe loop

if (0,0) in seen_points:
    print("ERROR (0,0) in pipe")

surface_seen = set()


points_to_check = []
seen_points_big = set()
data_big = []
for y in range(0, len(data)):
    data_big1 = []
    data_big2 = []
    data_big3 = []
    for x in range(0, len(data[0])):
        if data[y][x] == "|":
            data_big1.append(" ")
            data_big1.append("|")
            data_big1.append(" ")
            data_big2.append(" ")
            data_big2.append("|")
            data_big2.append(" ")
            data_big3.append(" ")
            data_big3.append("|")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+0, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+2, 3*x+1))
        elif data[y][x] == "-":
            data_big1.append(" ")
            data_big1.append(" ")
            data_big1.append(" ")
            data_big2.append("-")
            data_big2.append("-")
            data_big2.append("-")
            data_big3.append(" ")
            data_big3.append(" ")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+1, 3*x+0))
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+2))
        elif data[y][x] == "L":
            data_big1.append(" ")
            data_big1.append("|")
            data_big1.append(" ")
            data_big2.append(" ")
            data_big2.append("L")
            data_big2.append("-")
            data_big3.append(" ")
            data_big3.append(" ")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+0, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+2))
        elif data[y][x] == "J":
            data_big1.append(" ")
            data_big1.append("|")
            data_big1.append(" ")
            data_big2.append("-")
            data_big2.append("J")
            data_big2.append(" ")
            data_big3.append(" ")
            data_big3.append(" ")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+0, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+0))
                seen_points_big.add((3*y+1, 3*x+1))
        elif data[y][x] == "7":
            data_big1.append(" ")
            data_big1.append(" ")
            data_big1.append(" ")
            data_big2.append("-")
            data_big2.append("7")
            data_big2.append(" ")
            data_big3.append(" ")
            data_big3.append("|")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+1, 3*x+0))
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+2, 3*x+1))
        elif data[y][x] == "F":
            data_big1.append(" ")
            data_big1.append(" ")
            data_big1.append(" ")
            data_big2.append(" ")
            data_big2.append("F")
            data_big2.append("-")
            data_big3.append(" ")
            data_big3.append("|")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+2))
                seen_points_big.add((3*y+2, 3*x+1))
        elif data[y][x] == ".":
            data_big1.append("X")
            data_big1.append("X")
            data_big1.append("X")
            data_big2.append("X")
            data_big2.append("X")
            data_big2.append("X")
            data_big3.append("X")
            data_big3.append("X")
            data_big3.append("X")

        elif data[y][x] == "S":
            """
            data_big1.append(" ")
            data_big1.append(" ")
            data_big1.append(" ")
            data_big2.append(" ")
            data_big2.append("F")
            data_big2.append("-")
            data_big3.append(" ")
            data_big3.append("|")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+2))
                seen_points_big.add((3*y+2, 3*x+1))
            """
            data_big1.append(" ")
            data_big1.append("|")
            data_big1.append(" ")
            data_big2.append(" ")
            data_big2.append("|")
            data_big2.append(" ")
            data_big3.append(" ")
            data_big3.append("|")
            data_big3.append(" ")
            if (y,x) in seen_points:
                seen_points_big.add((3*y+0, 3*x+1))
                seen_points_big.add((3*y+1, 3*x+1))
                seen_points_big.add((3*y+2, 3*x+1))

    data_big.append(data_big1)
    data_big.append(data_big2)
    data_big.append(data_big3)
    
# vertical edges

for y in range(0, len(data_big)):
    for x in [0, len(data_big[0])-1]:
        if (y,x) not in seen_points_big:
            points_to_check.append((y,x))

for x in range(0, len(data_big[0])):
    for y in [0, len(data_big)-1]:
        if (y,x) not in seen_points_big:
            points_to_check.append((y,x))



            
while len(points_to_check):
    p = points_to_check.pop(0)

    surface_seen.add(p)
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            (test_y, test_x) = p
            test_y += y
            test_x += x

            # skip if out of bounds
            if test_x < 0 or test_y < 0:
                continue
            if test_x >= len(data_big[0]):
                continue
            if test_y >= len(data_big):
                continue

            # skip if we hit the pipe
            if (test_y, test_x) in seen_points_big:
                continue

            # skip if we already saw this one
            if (test_y, test_x) in surface_seen:
                continue

            # skip if already in the queue of things to check
            if (test_y, test_x) in points_to_check:
                continue
    
            points_to_check.append((test_y, test_x))

print(f"num tiles {len(data) * len(data[0])}. Num pipe {len(seen_points)}. Num surface {len(surface_seen)}")

for y in range(0, len(data_big)):

    print("")
    for x in range(0, len(data_big[0])):

        if (y,x) in seen_points_big:
            print('P', end='')

        elif (y,x) in surface_seen:
            print('O', end='')

        else:
            print('I', end='')

inside = 0
for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        y_start = y*3
        x_start = x*3

        i_seen = 0
        for y_delta in range(3):
            for x_delta in range(3):
                if (y_start + y_delta, x_start + x_delta) not in seen_points_big and (y_start + y_delta, x_start + x_delta) not in surface_seen:
                    i_seen += 1
        if i_seen == 9:
            inside += 1

print(f"Inside is {inside}")
