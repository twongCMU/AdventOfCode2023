import re

steps = "LRRRLRRLLRRLRRLRRLRRLRLLRLRLLRRLRLRRRLRRLRRLLRLRLRLRRRLRRRLLRLRRRLLRRRLRLLRRRLLRRLRLRLRRRLLRRLRRRLLRRLRLRRRLLRRRLRRLRLRRRLLRRLRRRLRRLLRRLRRLRRRLRRRLRRRLRRLRRRLLRLRLRLRRRLRRLRRRLRRLRLRRLRLRRRLRRRLRRLRRRLLRRRLLRRLRLRRRLRLRLRRRLRLRLRLRRLRLRRLRRLLRRRLRLLRRLRRRLRRRLLRRLRLLLLRRLRRRR"



filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()


network = {}
for l in lines:
    l = l.strip()
    if len(l) < 3:
        continue

    res = re.match(r"(.{3}) = \((.{3}), (.{3})\)", l)
    #print(f"{res.group(1)} -> {res.group(2)} , {res.group(3)}")
    network[res.group(1)] = {}

    network[res.group(1)]["L"] = res.group(2)
    network[res.group(1)]["R"] = res.group(3)



current_nodes = []
for n in network:
    if n[-1] == "A":
        current_nodes.append(n)



for n in current_nodes:
    print(f"Looking at {n}")
    steps_taken = 0
    instruction_index = 0
    current_node = n
    while current_node[-1] != "Z":
        instruction = steps[instruction_index]
        steps_taken += 1

        current_node = network[current_node][instruction]



        instruction_index += 1
        if instruction_index == len(steps):
            instruction_index = 0

    # I put all of these outputs into a lowest common multiple calculator website to get the final answer
    print(f"{n}: cycle time {steps_taken}")
    
print(f"Steps {steps_taken}")
