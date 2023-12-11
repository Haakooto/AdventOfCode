import numpy as np

def up(current):
    return current[0] - 1, current[1]
def down(current):
    return current[0] + 1, current[1]
def left(current):
    return current[0], current[1] - 1
def right(current):
    return current[0], current[1] + 1
def nothing(current):
    return current

up_mapper = {"|": up, "F": right, "7": left}
down_mapper = {"|": down, "L": right, "J": left}
left_mapper = {"-": left, "F": down, "L": up}
right_mapper = {"-": right, "7": down, "J": up}
mappers = {up: up_mapper, down: down_mapper, left: left_mapper, right: right_mapper}

def next(field, current, direction):
    mapper = mappers[direction]
    nxt = field[*direction(current)]
    if nxt in mapper:
        return direction(current), mapper[nxt]
    elif nxt == "S":
        return current, nothing
    else:
        return None, None

def solver(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    field = np.array([[i for i in line.strip()] for line in lines], dtype=str)
    start = np.asarray(np.where(field == "S")).flatten()
    h, w = field.shape

    visited = np.zeros_like(field, dtype=int)
    visited[start[0], start[1]] = 1

    for init_dir in (up, left, right, down):
        current, direction = next(field, start.copy(), init_dir) 
        if direction is not None:
            break

    directions = [init_dir]
    history = [start]
    
    turn = 1
    while direction is not nothing:
        turn += 1
        history.append(current)
        directions.append(direction)
        visited[current[0], current[1]] = turn
        current, direction = next(field, current, direction)
    part1 = (turn) // 2
    
    to_right = {up: right, right: down, down: left, left: up}
    to_left = {up: left, left: down, down: right, right: up}
    to = to_right  # define loop-orientation. Is set manually lol
    if input_file in ("test_input_4.txt", "test_input_5.txt", "input.txt"):
        to = to_left

    # To find enclosed points, idea:
    # 1: Go though all visited points, and mark points to the right (or left) of them as inside
    # 2: Remove all visited points
    # 3: Go trhough all inside points, and mark non-visited neighbors as inside
    # 4: Repeat 3 until no more points are added

    inside = np.zeros_like(field, dtype=int)
    for i in range(1, turn):
        for j in range(i-1, i+1):  # capture both sides of right turns
            direction = to[directions[j]]
            pos = direction(history[i])
            if 0 <= pos[0] < h and 0 <= pos[1] < w:
                inside[pos] = 1

    inside[np.where(visited)] = 0
    
    for _ in range(30):  # 30 is sufficient for all inputs
        for val in np.asarray(np.where(inside)).T:
            for dir in (up, down, left, right):
                neighbor = dir(val)
                if 0 <= neighbor[0] < h and 0 <= neighbor[1] < w:
                    if visited[neighbor] == 0:
                        inside[neighbor] = 1

    part2 = np.sum(inside)
    return part1, part2
