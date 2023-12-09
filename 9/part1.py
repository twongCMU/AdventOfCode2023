filename = "input.txt"

with open(filename) as f:
    lines = f.readlines()

sum = 0
for l in lines:
    data = []
    
    l.strip()
    if len(l) < 3:
        continue

    one_list = [int(x) for x in l.split(" ")]
    data.append(one_list)

    while max(one_list) != 0 or min(one_list) != 0:
        new_list = []
        for i in range(len(one_list) - 1):
            new_list.append(one_list[i+1] - one_list[i])

        data.append(new_list)
        one_list = new_list



    #print(f"{data}")
    
    #now extrapolate each one


    # now the first one is [0,0,0,0,..]
    data.reverse()
    
    print(f"data is {data}")
    adder = 0
    
    for v in data:
        adder = adder + v[-1]

    sum += adder

print(f"sum is {sum}")
    
    


    
