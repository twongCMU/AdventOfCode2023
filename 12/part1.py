
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


def build_possible(data):

    new_data = [data]
    new_data2 = []


    check_more = True
    while check_more:
        seen = set()
        check_more = False
        while len(new_data):
            n = new_data.pop(0)

            if "?" in n:
                #print(f"we here for {n}")
                check_more = True
                i = n.index("?")
                new_string = n[:i] + "." + n[i+1:]
                new_string2 = n[:i] + "#" + n[i+1:]

                if new_string not in seen:
                    new_data2.append(new_string)
                    seen.add(new_string)
                if new_string2 not in seen:
                    new_data2.append(new_string2)
                    seen.add(new_string2)
            else:
                if n not in seen:
                    new_data2.append(n)
                    seen.add(n)

        #print(f"one cycle from {len(new_data)} to {len(new_data2)} check more is {check_more}")
        new_data = new_data2.copy()
        new_data2 = []


    return new_data
    
with open(filename) as f:
    lines = f.readlines()

sum = 0
for l in lines:
    l = l.strip()

    if len(l) < 3:
        continue

    (data, res) = l.split(" ")

    all_possible = build_possible(data)
    good_count = 0
    for a in all_possible:
        if verify_data(a, res):
            good_count += 1
    print(f"Built {len(all_possible)} permutations for {data}, verified {good_count}")
    sum+=good_count


print(f"{sum}")
