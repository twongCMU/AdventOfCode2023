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


# compute one column at a time
total_sum = 0
for i in range(len(data[0])):

    column_sum = 0
    # if there is a O sliding up, the max value is the full height of the column
    cur_value = len(data)

    for v in range(len(data)):
        # v is the row within the column incrementing downward
        
        check_tile = data[v][i]
        if check_tile == "O":
            column_sum += cur_value
            cur_value -= 1 # next stone will push up against this one
        elif check_tile == "#":
            # get the value of the location of the #
            cur_value = len(data) - v
            # next stone will hit this so the cur_value is one fewer than this one
            cur_value -= 1

        # else is a "." tile which does nothing
    total_sum += column_sum
    
print(f"Total sum {total_sum}")

    
