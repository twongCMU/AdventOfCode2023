races = {
   48938595:296192812361391
}

wins = []
for (time, distance) in races.items():
    win_count = 0
    for i in range(time+1):
        charge = i
        run = time - i

        this_distance = charge * run

        if this_distance > distance:
            win_count += 1
    wins.append(win_count)

score = 1
for w in wins:
    score *= w
print(f"score {score}")
