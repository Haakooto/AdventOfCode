import numpy as np
from tqdm import tqdm

def north(input):
    for y, x in np.asarray(np.where(input == 2)).T:
        if y == 0:
            continue
        ray = input[:y, x][::-1]
        if len(space := np.where(np.cumsum(ray) == 0)[0]) > 0:
            moves = space[-1] + 1
            input[y - moves, x] = 2
            input[y, x] = 0
    return input

def south(input):
    return north(input[::-1])[::-1]

def west(input):
    return north(input.T).T

def east(input):
    return west(input[:, ::-1])[:, ::-1]

def cycle(input):
    return east(south(west(north(input))))

def parse_input(input_file):
    with open(input_file, "r") as file:
        board = (
            file.read()
            .replace(".", "0")
            .replace("#", "1")
            .replace("O", "2")
            .split("\n")[:-1]
        )
    return np.array([list(row) for row in board], dtype=int)

def solver_alt1(input_file, part2=False):
    board = parse_input(input_file)
    if part2:
        tot_cycles = 1000000000
        cache = [[], []]
        for i in tqdm(range(tot_cycles), leave=False):
            # cache[0].append(hash(board.tostring()))
            cache[1].append(board.copy())
            board = cycle(board)
            # hashed = hash(board.tostring())
            # if hashed in cache[0]:
            #     break

        period_start = cache[0].index(hashed)
        period_length = i - period_start + 1
        remainder = (tot_cycles - period_start) % period_length
        board = cache[1][period_start + remainder]
    else:
        board = north(board)

    load = 0
    for ind in range(1, board.shape[0] + 1):
        load += np.sum(board[-ind] == 2) * ind

    return load

def solver_alt2(input_file):
   
    return None, None

def solver1_alt3(input_file):
    return None

def solver2_alt3(input_file):
    return None
