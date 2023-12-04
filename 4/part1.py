import re

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

total_score = 0
for l in lines:
    l = l.strip()
    if len(l) < 2:
        continue
    
    matches = re.match(r"Card\s+(\d+):\s+(.+)", l)
    # group 1 = card number
    # group 2 = rest of data

    card = int(matches.group(1))
    data = matches.group(2)

    (winning_string, have_string) = data.split("|")

    winning_numbers = set([int(x) for x in re.findall(r"(\d+)", winning_string)])
    have_numbers = [int(x) for x in re.findall(r"(\d+)", have_string)]

    print(f"card {card} haves {have_numbers}")
    winning_score = 0
    for h in have_numbers:
        if h in winning_numbers:
            if winning_score == 0:
                winning_score = 1
            else:
                winning_score *= 2


    total_score += winning_score
print(f"{total_score}")

    
    

    
                                 
