import copy 
filename = "input.txt"


with open(filename) as f:
    lines = f.readlines()


data = []
for l in lines:
    l = l.strip()
    if len(l) < 3:
        continue


    one_row = [x for x in l]
    data.append(one_row)

# long thing is either a row or a column
def tilt_one(long_thing):
    # this mutates the input vector
    first_opening = 0
            
    # tilt toward the lower index of the long_thing
    for v in range(len(long_thing)):

        check_tile = long_thing[v]
        if check_tile == "#":
            # if we see a "#" then the next opening is below it
            first_opening = v+1
        elif check_tile == "O":
            # nothing to move since the stone is already in the best position
            if v == first_opening:
                first_opening += 1
                continue

            # if the stone can slide, swap it with an open spot
            long_thing[v] = "."
            long_thing[first_opening] = "O"
            #print(f"moving from {v} to {first_opening}")
            # next stone can fit one below where we just slid one into
            first_opening += 1

def tilt_north(data):
    for i in range(len(data[0])):
        long_thing = []
        for v in range(len(data)):
            long_thing.append(data[v][i])
        tilt_one(long_thing)
        for v in range(len(data)):
            data[v][i] = long_thing[v]

# same as north but long_thing is reversed
def tilt_south(data):
    for i in range(len(data[0])):
        long_thing = []
        for v in range(len(data)):
            long_thing.append(data[v][i])
        long_thing.reverse()
        tilt_one(long_thing)
        long_thing.reverse()
        for v in range(len(data)):
            data[v][i] = long_thing[v]

def tilt_west(data):
    # for each row, tilt it left
    for i in range(len(data)):
        long_thing = []
        for v in range(len(data[0])):
            long_thing.append(data[i][v])
        tilt_one(long_thing)
        for v in range(len(data[0])):
            data[i][v] = long_thing[v]

# same as west, but long_thing is reversed
def tilt_east(data):
    # for each row, tilt it left
    for i in range(len(data)):
        long_thing = []
        for v in range(len(data[0])):
            long_thing.append(data[i][v])
        long_thing.reverse()
        tilt_one(long_thing)
        long_thing.reverse()
        for v in range(len(data[0])):
            data[i][v] = long_thing[v]
            
def score_north(data):
    # compute one column at a time
    total_sum = 0
    for i in range(len(data[0])):
        
        for v in range(len(data)):
            check_tile = data[v][i]
            if check_tile == "O":
                total_sum += len(data) - v

    return total_sum

def print_data(data):
    for v in range(len(data)):
        print("")
        for i in range(len(data[0])):
            print(f"{data[v][i]}", end='')

def get_coords(data):
    coords = ""
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "O":
                coords += f"{i}_{j}__"
    print(f"coords is {coords}")
    return coords

seen = {}
scores = {}
print_data(data)
for i in range(1000000000):
    tilt_north(data)
    tilt_west(data)
    tilt_south(data)
    tilt_east(data)
    print(" ")
    print_data(data)
    print(" ")
    coords = get_coords(data)
    scores[i] = score_north(data)
    
    if coords in seen:
        print(f"Found cycle at {i}!")
        print(f"Last seen {seen[coords]}")
        print_data(data)
        loop_start = seen[coords]
        loop_end = i
        break
    else:
        seen[coords] = i

print(f"loop start at {loop_end}, saw {loop_start} with score {scores[loop_start]}")

    
total_cycles = 1000000000
total_cycles -= loop_start
full_cycles = int(total_cycles/(loop_end-loop_start))
remainder = total_cycles % (loop_end-loop_start)

desired_index = loop_start + remainder - 1
print(f"full cycles {full_cycles} remainder {remainder} {scores[desired_index]}")

print(f"scores dump is {scores}")
