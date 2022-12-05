inp = open("input", "r").read().strip().split("\n")
score = 0

for game in inp:
    you, me = game.split()
    game_score = 0

    # Lord forgive me for this
    if you == "A":      # rock
        if me == "X":       # lose
            game_score += 3          # scissor
        elif me == "Y":     # draw
            game_score += 4          # rock
        else:               # win
            game_score += 8          # paper
    elif you == "B":    # paper
        if me == "X":       # lose
            game_score += 1          # rock
        elif me == "Y":     # draw
            game_score += 5          # paper
        else:               # win
            game_score += 9          # scissor
    else:               # scissor
        if me == "X":       # lose
            game_score += 2          # paper
        elif me == "Y":     # draw
            game_score += 6          # scissor
        else:               # win
            game_score += 7          # rock

    score += game_score

print(score)