# worked backwards by testing locations from 0->n to see if the resulting seed was in the seeds list
# but even that was slow so I incremented cur_value +=1000 to hone in on the solution and found it was
# between 69841000 and 69842000, then set cur_value to 69841000and ran it with increment +=1


import datetime
seeds = [(2906422699,6916147),(3075226163,146720986),(689152391,244427042),(279234546,382175449),(1105311711,2036236),(3650753915,127044950),(3994686181,93904335),(1450749684,123906789),(2044765513,620379445),(1609835129,60050954)]

mappings = {}
            
filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

def build_data(data, current_key, dest_start, source_start, range_len):
    data[current_key][(source_start, source_start+range_len)] = dest_start

def lookup_data(data, current_key, value):
    for r in data[current_key]:
        (source_start, source_end) = r
        dest_start = data[current_key][r]
        dest_end = dest_start + source_end - source_start

        if dest_start <= value < dest_end:
            diff = value - dest_start
            return source_start + diff

    return value
    
data = {}
current_key = None
for l in lines:
    l = l.strip()
    if len(l) < 2:
        continue

    if "map" in l:
        current_key = l.split(" ")[0]
        (source_key, dest_key) = current_key.split("-to-")
        mappings[dest_key] = source_key
        data[current_key] = {}
        print(f"Getting map {current_key}")
    else:
        (dest_start, source_start, range_len) = l.split(" ")
        dest_start = int(dest_start)
        source_start = int(source_start)
        range_len = int(range_len)
        print(f"Building ranges {dest_start} {source_start} {range_len}")
        build_data(data, current_key, dest_start, source_start, range_len)





cur_value = 69841000
not_found = True
while not_found:
    dest_key = "location"

    test_value = cur_value
    while dest_key != "seed":
        source_key = mappings[dest_key]
        full_key = f"{source_key}-to-{dest_key}"

        dest_key = source_key
        test_value = lookup_data(data, full_key, test_value)
        


    # now test_value is a seet. Let's see if it is in the list of seeds
    for s in seeds:
        (s_start, s_len) = s
        if s_start <= test_value < s_start + s_len:
            print(f"lowest location is {cur_value}")
            not_found=False
            break
    print(f"Testing {cur_value} seed was {test_value}")
    cur_value += 1
        
