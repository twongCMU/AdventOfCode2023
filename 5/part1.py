

seeds = [2906422699,6916147,3075226163,146720986,689152391,244427042,279234546,382175449,1105311711,2036236,3650753915,127044950,3994686181,93904335,1450749684,123906789,2044765513,620379445,1609835129,60050954]

mappings = {}
            
filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

def build_data(data, current_key, dest_start, source_start, range_len):
    data[current_key][(source_start, source_start+range_len)] = dest_start

def lookup_data(data, current_key, value):
    for r in data[current_key]:
        (source_start, source_end) = r
        if source_start <= value < source_end:
            diff = value - source_start
            return data[current_key][r] + diff

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
        mappings[source_key] = dest_key
        data[current_key] = {}
        print(f"Getting map {current_key}")
    else:
        (dest_start, source_start, range_len) = l.split(" ")
        dest_start = int(dest_start)
        source_start = int(source_start)
        range_len = int(range_len)
        print(f"Building ranges {dest_start} {source_start} {range_len}")
        build_data(data, current_key, dest_start, source_start, range_len)


lowest = 9999999999999999999
for s in seeds:
    source_key = "seed"
    value = s
    while source_key != "location":
        dest_key = mappings[source_key]
        full_key = f"{source_key}-to-{dest_key}"

        source_key = dest_key
        value = lookup_data(data, full_key, value)

    if value < lowest:
        lowest = value
print(f"Lowest is {lowest}")


        

    
        

    
