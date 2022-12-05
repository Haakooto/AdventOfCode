inp = open("input", "r").read().strip().split("\n")
score = 0

pick = {"X": 1, "Y": 2, "Z": 3}

for game in inp:
    you, me = game.split()
    game_score = pick[me]

    # Lord forgive me for this
    if you == "A":      # rock
        if me == "X":       # rock
            game_score += 3          # draw
        elif me == "Y":     # paper
            game_score += 6          # win
        else:               # scissor
            game_score += 0          # lose
    elif you == "B":    # paper
        if me == "X":       # rock
            game_score += 0          # lose
        elif me == "Y":     # paper
            game_score += 3          # draw
        else:               # scissor
            game_score += 6          # win
    else:               # scissor
        if me == "X":       # rock
            game_score += 6          # win
        elif me == "Y":     # paper
            game_score += 0          # lose
        else:               # scissor
            game_score += 3          # draw

    score += game_score

print(score)