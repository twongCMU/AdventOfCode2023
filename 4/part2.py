import re

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

card_score = {}
card_count = {}
for l in lines:
    l = l.strip()
    if len(l) < 2:
        continue
    
    matches = re.match(r"Card\s+(\d+):\s+(.+)", l)
    # group 1 = card number
    # group 2 = rest of data

    card = int(matches.group(1))
    data = matches.group(2)

    if card not in card_count:
        card_count[card] = 1
    else:
        # could already have a copy of the card from a previous winning
        card_count[card] += 1
    
    (winning_string, have_string) = data.split("|")

    winning_numbers = set([int(x) for x in re.findall(r"(\d+)", winning_string)])
    have_numbers = [int(x) for x in re.findall(r"(\d+)", have_string)]

    print(f"card {card} haves {have_numbers}")
    winning_score = 0
    winning_count = 0
    for h in have_numbers:
        if h in winning_numbers:
            winning_count += 1
            if winning_score == 0:
                winning_score = 1
            else:
                winning_score *= 2


    card_score[card] = winning_score
    
    for index in range(winning_count):
        card_offset = card + 1 + index
        if card_offset not in card_count:
            card_count[card_offset] = card_count[card]
        else:
            card_count[card_offset] += card_count[card]

            
total_cards = 0
for valid_card in card_score:
    total_cards += card_count[valid_card]

print(f"card cout {card_count}")
print(f"Total {total_cards}")

    
    

    
                                 
