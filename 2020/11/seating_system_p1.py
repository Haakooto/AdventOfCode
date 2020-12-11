import numpy as np

analogue = np.loadtxt("i", dtype=int, converters={0:lambda s: [i for i in s]}, ndmin=2)
layout = np.zeros_like(analogue)
layout = np.where(analogue == 46, np.nan, layout)

X, Y = layout.shape

def game_of_seats(room):
    temp = np.zeros((X + 2, Y + 2))
    temp[1:-1, 1:-1] = room
    changed = False

    for i in range(X):
        for j in range(Y):
            adjacent = np.nansum(temp[i: i + 3, j: j + 3])

            if room[i, j] == 1:
                if adjacent > 4:
                    room[i, j] = 0
                    changed = True
            elif room[i, j] == 0:
                if adjacent == 0:
                    room[i, j] = 1
                    changed = True
    return changed

while game_of_seats(layout):
    continue
print(np.nansum(layout))