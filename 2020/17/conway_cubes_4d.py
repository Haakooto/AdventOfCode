import numpy as np

analogue = np.loadtxt("input", dtype=int, comments=None, converters={0: lambda s: [i for i in s]}, ndmin=2)

active = []
for y, col in enumerate(analogue):
    for x, cube in enumerate(col):
        if cube == 35:
            active.append((x, y, 0, 0))

diff = np.arange(-1, 2)
diffs = []
for dx in diff:
    for dy in diff:
        for dz in diff:
            for dw in diff:
                if not (dx == dy == dz == dw == 0):
                    diffs.append((dx, dy, dz, dw))


def game_of_cubes(active):
    neighbours = {}
    for cell in active:
        if cell not in neighbours:
            neighbours[cell] = 0
        for neigh in get_neighs(*cell):
            if neigh in neighbours:
                neighbours[neigh] += 1
            else:
                neighbours[neigh] = 1

    new = []
    for cell, neighs in neighbours.items():
        if cell in active:
            if neighs in (2, 3):
                new.append(cell)
        else:
            if neighs == 3:
                new.append(cell)
    return set(new)


def get_neighs(x, y, z, w):
    neighs = []
    for dx, dy, dz, dw in diffs:
        neighs.append((x + dx, y + dy, z + dz, w + dw))
    return neighs


for i in range(6):
    active = game_of_cubes(active)
print(len(active))