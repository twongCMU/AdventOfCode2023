import functools




filename="input.txt"

values = {"J":1,
          "2":2,
          "3":3,
          "4":4,
          "5":5,
          "6":6,
          "7":7,
          "8":8,
          "9":9,
          "T":10,
          #"J":11,
          "Q":12,
          "K":13,
          "A":14,
          }
          
          
def is_full_house(hand):
    if 3 in hand.values() and 2 in hand.values():
        return True
    return False

def is_three_of_kind(hand):
    if 3 in hand.values() and not 2 in hand.values():
        return True
    return False

def is_two_pair(hand):
    pairs = 0
    for v in hand.values():
        if v == 2:
            pairs += 1
    if pairs == 2:
        return True
    return False

def is_one_pair(hand):
    pairs = 0
    for v in hand.values():
        if v == 2:
            pairs += 1
    if pairs == 1:
        return True
    return False

def highest_key(x_dist):
    h_k = 0
    h_v = 0

    for (k,v) in x_dist.items():
        if v > h_v:
            h_v = v
            h_k = k
    return h_k
    
def compare(x, y):
    x_dist = {}
    y_dist = {}
    x_j = 0
    y_j = 0
    for c in x:
        if c == "J":
            x_j += 1
            continue
        if c not in x_dist:
            x_dist[c] = 1
        else:
            x_dist[c] += 1

    for c in y:
        if c == "J":
            y_j += 1
            continue
        if c not in y_dist:
            y_dist[c] = 1
        else:
            y_dist[c] += 1


    # The dataset is evil and one card is JJJJJ so it shows up as no cards in x_dist
    # and 5 jokers and gets confused so we just override that one case
    if len(x_dist) == 0:
        x_dist["J"] = 5
        x_j=0
    if len(y_dist) == 0:
        y_dist["J"] = 5
        y_j=0
        
    x_key = highest_key(x_dist)
    x_dist[x_key] += x_j

    y_key = highest_key(y_dist)
    y_dist[y_key] += y_j
    
    # handle 5 of a kind
    if max(x_dist.values()) == 5 and max(y_dist.values()) < 5:
        return 1
    if max(y_dist.values()) == 5 and max(x_dist.values()) < 5:
        return -1

    # handle 4 of a kind
    if max(x_dist.values()) == 4 and max(y_dist.values()) < 4:
        return 1
    if max(y_dist.values()) == 4 and max(x_dist.values()) < 4:
        return -1

    # handle full house
    if is_full_house(x_dist) and not is_full_house(y_dist):
        return 1
    if is_full_house(y_dist) and not is_full_house(x_dist):
        return -1

    # handle 3 of a kind not full house
    if is_three_of_kind(x_dist) and not is_three_of_kind(y_dist):
        return 1
    if is_three_of_kind(y_dist) and not is_three_of_kind(x_dist):
        return -1

    # handle 2 pair
    if is_two_pair(x_dist) and not is_two_pair(y_dist):
        return 1
    if is_two_pair(y_dist) and not is_two_pair(x_dist):
        return -1

    # handle 1 pair
    if is_one_pair(x_dist) and not is_one_pair(y_dist):
        return 1
    if is_one_pair(y_dist) and not is_one_pair(x_dist):
        return -1
    
    for i in range(5):
        if values[x[i]] > values[y[i]]:
            return 1
        if values[y[i]] > values[x[i]]:
            return -1

    return 0
    
with open(filename) as f:
    lines = f.readlines()



data = {}
for l in lines:
    l = l.strip()
    if len(l) < 2:
        continue

    (hand, value) = l.split(" ")
    value = int(value)
    data[hand] = value

hand_list = data.keys()

hand_list_sorted = sorted(hand_list, key=functools.cmp_to_key(compare))


rank = 1
sum = 0
for v in hand_list_sorted:
    sum += rank * data[v]
    rank+=1
    
print(f"Part 1 {sum}")
print(f"ranks {hand_list_sorted}")
