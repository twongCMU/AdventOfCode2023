filename="input.txt"

with open(filename) as f:
    lines = f.readlines()


def hash_string(input):
    current_value = 0
    
    for v in input:
        ascii_code = ord(v)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value


sum = 0
for l in lines:
    l = l.strip()
    if len(l) < 3:
        continue


    commands = l.split(",")
    for c in commands:
        sum += hash_string(c)

print(f"{sum}")
