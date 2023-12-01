import re

file="input.txt"
with open(file) as f:
    line = f.readlines()


sum = 0
for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

    res = re.findall(r"([0-9])", v)
    print(f"{v} : {res}")
    sum += 10*int(res[0])
    sum += int(res[-1])

print(f"Part 1: {sum}")
