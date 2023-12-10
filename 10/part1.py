
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

start_points = [(start_y+1, start_x), (start_y-1, start_x)]
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

print(f"Ended at {start_points} distance {distance}")
