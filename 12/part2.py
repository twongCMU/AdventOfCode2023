
filename = "input.txt"


def verify_data(data, groups):
    d = data.split(".")
    d_filtered = []
    for d_one  in d:
        if len(d_one) >= 1:
            d_filtered.append(d_one)
            
    g = [int(x) for x in groups.split(",")]

    if len(g) != len(d_filtered):
        return False


    for i, one_group in enumerate(g):
        if len(d_filtered[i]) != g[i]:
            return False


    return True


def is_data_possible(data, groups):
    d = data.split(".")
    d_filtered = []
    for d_one  in d:
        if len(d_one) >= 1:
            d_filtered.append(d_one)

    g = [int(x) for x in groups.split(",")]

    # sloppy but if our test string has more groups than the solution then we can drop it
    d_no_q = []
    for d_one  in d:
        if "?" not in d_one and len(d_one) >= 1:
            d_no_q.append(d_one)
    if len(d_no_q) > len(g):
        return False

    #print(f"Checking {data} vs {groups}")
    # check each group until we reach a ?
    for i, one_group in enumerate(d_filtered):
        one_group = d_filtered[i]

        # If there is a ? here we don't know check # up to the ?
        if "?" in one_group:
            #print(f"{data} could match requested {g}")
            return True

        if len(g) > i and len(d_filtered[i]) != g[i]:
            #print(f"{data} cannot match requested {g}")
            return False

    #print(f"Fell out, keeping {data}")
    return True


def compute_groups(one_data):
    d = one_data.split(".")
    d_filtered = []
    for d_one  in d:
        if len(d_one) >= 1:
            d_filtered.append(d_one)

    return d_filtered

def group_to_string(g):
    ret = ""
    for v in g:
        ret += f"{v}_"

    return ret

def print_data(data, groups):
    k = list(data.keys())[0:10]
    for d in k:
        #print(f"{d} {compute_groups(d)} {data[d]}")
        print(f"{d} {data[d]} goal {groups}")

def update_data(data, new_string, how_many):
    g = compute_groups(new_string)
    g_str = group_to_string(g)
    found = False
    #print(f"candidate {new_string}")
    if g_str in data:
        (old_g, old_v) = data[g_str]
        #print(f"Adding to existing {g_str}")
        data[g_str] = (new_string, old_v + how_many)
    else:
        #print(f"Adding as new ")
        data[g_str]= (new_string, how_many)
    
def build_possible(data, groups):

    new_data = {}
    g = compute_groups(data)
    # group -> (data, count)
    g_str = group_to_string(g)
    new_data[g_str] = (data, 1)

    new_data2 = {}


    check_more = True
    while check_more:
        #seen = set()
        check_more = False
        new_data_keys = list(new_data.keys())
        for k in new_data_keys:
            (v, n) = new_data.pop(k)

            #print(f"considering {k}")
            if "?" in v:
                check_more = True
                i = v.index("?")
                new_string = v[:i] + "." + v[i+1:]
                new_string2 = v[:i] + "#" + v[i+1:]

                new_string_possible = is_data_possible(new_string, groups)
                new_string_possible2 = is_data_possible(new_string2, groups)

                if new_string_possible:
                    update_data(new_data2, new_string, n)


                if new_string_possible2:
                    update_data(new_data2, new_string2, n)


            else:
                update_data(new_data2, v, n)

        #print(f"one cycle now {len(new_data2)} check more is {check_more}")
        #print_data(new_data2, groups)
        new_data = new_data2.copy()
        new_data2 = {}


    return new_data
    
with open(filename) as f:
    lines = f.readlines()

sum = 0
for l in lines:
    l = l.strip()

    if len(l) < 3:
        continue

    (data, res) = l.split(" ")

    # part 2 stipulation
    data = data + "?" + data + "?" + data + "?" + data + "?" + data
    res = res + "," + res + "," + res + "," + res + "," + res

    
    all_possible = build_possible(data, res)
    good_count = 0
    for a, (s, v) in all_possible.items():
        if verify_data(s, res):
            good_count += v
    print(f"Built {len(all_possible)} permutations for {data}, verified {good_count}")
    print("----------------------------")
    sum+=good_count


print(f"{sum}")
