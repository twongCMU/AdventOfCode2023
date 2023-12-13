import copy

filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()


def check_data(data):

    check_after_rows = 1
    rets = []
    # check each row as the possible mirror point
    #print(f"box is {len(data)} high and width is {len(data[0])}")
    for check_after_rows in range(1, len(data)):
        found_mirror = True
        
        check_rows = min(check_after_rows, len(data)-check_after_rows)

        data_top_start = check_after_rows-1
        data_bottom_start = check_after_rows

        
        #print(f" ranges are {check_after_rows - check_rows}:{check_after_rows} and {check_after_rows}:{check_after_rows + check_rows}")

        # check each pair of rows eminating from the mirror point
        for i in range(check_rows):
            data_top_check = data_top_start - i
            data_bottom_check = data_bottom_start + i
            #print(f"check row is {check_after_rows} and {data_top_check}{data[data_top_check]} {data_bottom_check}{data[data_bottom_check]}")
            if data[data_top_check] != data[data_bottom_check]:
                found_mirror = False
                break
        if found_mirror is True and check_after_rows not in rets:
            rets.append(check_after_rows)

    if len(rets) > 0:
        return rets
    return -1

def check_all_data(data, one_score):
    ret = check_data(data)
    if ret != -1:
        for v in ret:
            if (100*v) != one_score:
                return 100* v

    rotated_data = rotate_left(data)

    #print_data(data)
    #print("Rotated data")
    #print_data(rotated_data)
    ret = check_data(rotated_data)
    if ret != -1:
        for v in ret:
            real_ret = len(data[0]) - v
            if real_ret != one_score:
                # nth row down pre-rotation is nth row from the right

                return real_ret

    return -1

def print_data(data):
    for r in data:
        print(f"{r}")
        
def rotate_left(data):
    rotated_data = []

    data_h = len(data)
    data_w = len(data[0])

    rotated_data_w = data_h
    rotated_data_h = data_w

    for i in range(rotated_data_h):
        rotated_data.append([])

    for y, r in enumerate(data):
        for x, v in enumerate(r):
            rotated_x = y
            rotated_y = rotated_data_h-x-1
            rotated_data[rotated_y].append(v)
    return rotated_data
            

def enumerate_replacements(data, one_score):
    for i in range(len(data)):
        for j in range(len(data[0])):
            print(f"Trying {i}{j}")
            
            data_copy = copy.deepcopy(data)
            if data_copy[i][j] == ".":
                data_copy[i][j] = "#"
            else:
                data_copy[i][j] = "."
            print_data(data_copy)
            new_score = check_all_data(data_copy, one_score)
            print(f"Got newscore {new_score}")
            if new_score != -1 and new_score != one_score:
                return new_score

   
data = []
score = 0
box = 1
for l in lines:
    l = l.strip()

    if len(l) < 3:
        print(f"Scoring box {box}")
        box += 1

        # Get original score
        one_score = check_all_data(data, -1)
        new_score = enumerate_replacements(data, one_score)
                    
        print(f"score {new_score}")
        score+=new_score
        data = []
    else:
        one_line = [x for x in l]
        data.append(one_line)

one_score = check_all_data(data, -1) 
print(f"Original score {one_score} {len(data)}x{len(data[0])}")
new_score = enumerate_replacements(data, one_score)
print(f"score {new_score}")
score+=new_score
print(f"sum is {score}")


    
