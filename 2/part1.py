
filename = "input.txt"
with open(filename) as f:
    line = f.readlines()

limits = {"red":12,
          "green":13,
          "blue":14
          }

total_sum = 0
for l in line:
    v = l.strip()
    if len(v) == 0:
        continue
    
    # A line
    (game, values) = v.split(": ")
    game_id = int(game[len("Game "):])

    pulls = values.split("; ")
    valid = True
    
    for p in pulls:
        color_values = p.split(", ")

        for c in color_values:
            (number, color) = c.split(" ")
            number = int(number)

            if number > limits[color]:
                valid = False
                print(f"game {game_id} violation {color} saw {number} > limit {limits[color]}")
                break
            
        if not valid:
            break
        

    if valid:
        total_sum += game_id

    print(f"Game {game_id}: {total_sum}")
          
          
        
