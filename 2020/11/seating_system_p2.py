import numpy as np
from itertools import permutations

analogue = np.loadtxt("i", dtype=int, converters={0:lambda s: [i for i in s]}, ndmin=2)
layout = np.zeros_like(analogue)
layout = np.where(analogue == 46, np.nan, layout)

X, Y = layout.shape


def game_of_seats(room, verb=False):
    temp = np.zeros((X + 2, Y+2))
    temp[1: -1, 1: -1] = room

    changed = False
    for i in range(X):
        for j in range(Y):
            if np.isnan(room[i, j]):
                continue
            see = 0
            for dx, dy in [(1, 1), (-1, -1)] + list(permutations([-1, 0, 1], 2)):
                x, y = dx, dy
                while np.isnan(temp[1 + i + x, 1 + j + y]):
                    x += dx
                    y += dy
                    if (1 + i + x) in (0, X + 1) or (1 + j + y) in (0, Y + 1):
                        break
                see += temp[1 + i + x, 1 + j + y]

            if room[i, j] == 1:
                if see >= 5:
                    room[i, j] = 0
                    changed = True
            elif room[i, j] == 0:
                if see == 0:
                    room[i, j] = 1
                    changed = True

    return changed


while game_of_seats(layout):
    continue
print(np.nansum(layout))