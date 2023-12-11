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

    insides = 0
    for candidate in np.asarray(np.where(visited == 0)).T:
        if 1 <= candidate[0] < h-1 and 1 <= candidate[1] < w-1:
            chain = visited[candidate[0], candidate[1]+1:] != 0
            ray = "".join(field[candidate[0], candidate[1]+1:][chain])
            ray = ray.replace("-", "").replace("FJ", "|").replace("L7", "|")
            if len(ray) % 2 != 0:
                insides += 1
                
    return part1, insides
    