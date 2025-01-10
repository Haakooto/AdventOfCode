from collections import defaultdict

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]

def make_ordering(maze):
    rows, cols = len(maze), len(maze[0])
    pos = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                pos = (r, c)
                break
        if pos:
            break
    
    points = {}
    i = 0
    while True:
        points[pos] = i
        i += 1
        if maze[pos[0]][pos[1]] == "E":
            break
        for d in ((0, 1), (0, -2), (1, 1), (-2, 0)):
            pos = pos[0] + d[0], pos[1] + d[1]
            if pos not in points and maze[pos[0]][pos[1]] != "#":
                break
    return points

def search(point, dist):
    cands = []
    x, y = point
    for dx in range(-dist, dist+1):
        for dy in range(-dist, dist+1):
            dd = abs(dx) + abs(dy)
            if dd > dist:
                continue
            if dx == dy == 0:
                continue
            cands.append(((x+dx, y+dy), dd))
    return cands

def solver(input_file, part2=False):
    lines = read(input_file)
    points = make_ordering(lines)
    saves = defaultdict(int)

    for p in points.keys():
        for dp, dd in search(p, 20 if part2 else 2):
            if dp in points:
                diff = points[dp] - points[p] - dd
                if diff > 0:
                    saves[diff] += 1

    good = 0        
    for s, c in saves.items():
        if s >= 100:
            good += c
    return good 
