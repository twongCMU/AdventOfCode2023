
filename = "input.txt"
with open(filename) as f:
    line = f.readlines()


total_sum = 0
for l in line:
    minimums = {
        "blue":0,
        "red":0,
        "green":0
    }
    
    v = l.strip()
    if len(v) == 0:
        continue
    
    # A line
    (game, values) = v.split(": ")
    game_id = int(game[len("Game "):])

    pulls = values.split("; ")
    
    for p in pulls:
        color_values = p.split(", ")

        for c in color_values:
            (number, color) = c.split(" ")
            number = int(number)

            if number > minimums[color]:
                minimums[color] = number
            

        

    total_sum += minimums["red"] * minimums["green"] * minimums["blue"]

    print(f"Game {game_id}: {total_sum}")
          
          
        
