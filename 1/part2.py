import re

# We can't regsub the entire string because sometimes letters overlap like
# eightwo which should result in 82. This solution recognizes that
# numbers only ever overlap by one letter so we just remove one letter
# from each word. However doing them in numberical order has "ne"->1
# then "ine"->9 and the "ne" matches the substring in "ine" and we swap
# the order to match 9 first since it's a longer unique string. Credit to
# Me-me for this brilliant solution.
numbers_dict = {"ine":9,
                "wo":2,
                "hree":3,
                "our":4,
                "ive":5,
                "ix":6,
                "even":7,
                "ight":8,
                "ne":1}
file="input.txt"
with open(file) as f:
    line = f.readlines()


sum_part2 = 0
for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

    for word, value in numbers_dict.items():
        v = re.sub(word, str(value), v)
    print(f"v is: {v}")
        
    res = re.findall(r"([0-9])", v)
    print(f"{res}")
    sum_part2 += 10*int(res[0])
    sum_part2 += int(res[-1])

print(f"Part 2: {sum_part2}")
