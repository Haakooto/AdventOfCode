import numpy as np
from tqdm import tqdm

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    # One function that behaves differently depending on part2
    return None

def visit(map, pos, new_pos):
    a, b = pos[:, 0]
    c, d = new_pos[:, 0]
    rs, re = sorted([a, c])
    cs, ce = sorted([b, d])
    map[rs:re+1, cs:ce+1] = 1

def simulate(map, loop=False):
    cols, rows = map.shape
    pos = np.asarray(np.where(map==94))
    visits = np.zeros_like(map)
    dirs = {}
    obstacles = np.asarray(np.where(map==35))
    direction = np.array([-1, 0])[:, None]  # up
    turn = lambda d: (d[:, 0] @ np.array([[0, -1], [1, 0]]))[:, None]
    t = lambda d: tuple(d[:, 0])
    for i in range(4):
        direction = turn(direction)
        dirs[t(direction)] = []

    while True:
        axis = np.where(direction == 0)[0][0] # get x (0) or y (1) axis
        n = np.where(obstacles[axis] == pos[axis])  # ids of obstacles ahead
        diffs = ((obstacles[axis-1, n] - pos) * direction)[axis-1]

        # This ugly-ass block only iterates you out of the labyrinth when you only have blue skies ahead
        if (diffs < 0).all():
            if loop:  # for part 2, knowing you can escape is enough
                return None, False
            end = pos.copy()
            up = True
            down = True
            while up and down:  # could calculate directly, but while-loop goes brrrr
                pos += direction
                up = (np.zeros(2) < pos[:, 0]).all()
                down = (pos[:, 0] < np.array([cols, rows])).all()
            visit(visits, end, pos)
            break

        i = np.min(diffs[diffs > 0]) * direction
        new_pos = pos + i - direction
        visit(visits, pos, new_pos)

        # memory and cheks for part 2
        if t(new_pos) in dirs[t(direction)] and loop:
            return None, True
        dirs[t(direction)].append(t(new_pos))

        pos = new_pos
        direction = turn(direction)
    return visits, None


def solver_alt2(input_file):
    lines = read(input_file)
    rows, cols = len(lines), len(lines[0])
    map = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            map[r, c] = ord(lines[r][c])
    
    pos = np.asarray(np.where(map==94))
    visits, _ = simulate(map)
    loops = 0
    candidates = np.asarray(np.where(visits == 1))
    for cand in tqdm(candidates.T):
        if (pos[:, 0] == cand).all():
            continue
        _map = map.copy()
        _map[*cand] = 35
        _, loop = simulate(_map, loop=True)
        if loop:
            loops += 1


    count = int(np.sum(visits))
    return count, loops

def solver1_alt3(input_file):
    lines = read(input_file)
    return None 

def solver2_alt3(input_file):
    lines = read(input_file)
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
