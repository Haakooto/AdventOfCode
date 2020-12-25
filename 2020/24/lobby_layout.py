tiles = {}
for tile in open("input").read().strip().splitlines():
    x = 0
    y = 0
    z = 0

    i = 0
    while i != len(tile):
        if (l:=tile[i]) == "e":
            x += 1
            y -= 1
        elif l == "w":
            x -= 1
            y += 1
        elif l == "s":
            i += 1
            if tile[i] == "w":
                x -= 1
                z += 1
            elif tile[i] == "e":
                y -= 1
                z += 1
        elif l == "n":
            i += 1
            if tile[i] == "w":
                y += 1
                z -= 1
            elif tile[i] == "e":
                x += 1
                z -= 1
        i += 1
    if (til := (x, y, z)) in tiles:
        tiles[til] = not tiles[til]
    else:
        tiles[til] = True

print(sum(tiles.values()))


def game_of_tiles(tils):
    adjacents = {}
    for til in tils:
        for neigh in get_adjacent(*til):
            if neigh not in adjacents:
                adjacents[neigh] = 0
            adjacents[neigh] += tils[til]
    new = {}
    for til, neighs in adjacents.items():
        if til in tils:
            if tils[til]:
                if neighs in (1, 2):
                    new[til] = True
            else:
                if neighs == 2:
                    new[til] = True
        else:
            if neighs == 2:
                new[til] = True
    return new


def get_adjacent(x, y, z):
    adjs = []
    for dx, dy, dz in ((0, -1, 1),  (0, 1, -1), (1, 0, -1), (-1, 0, 1), (1, -1, 0), (-1, 1, 0)):
        adjs.append((x + dx, y + dy, z + dz))
    return adjs


for _ in range(100):
    tiles = game_of_tiles(tiles)
print(sum(tiles.values()))