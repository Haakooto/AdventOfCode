import re
import numpy as np

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def diagonals(lines):
    rows, cols = len(lines), len(lines[0])
    new_lines = []
    for c in range(cols-4, -1, -1):
        d = ""
        for r in range(0, rows-c):
            d += lines[r][c+r]
        new_lines.append(d)
    for r in range(rows-4, 0, -1):
        d = ""
        for c in range(0, cols-r):
            d += lines[r+c][c]
        new_lines.append(d)
    return new_lines

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    # One function that behaves differently depending on part2
    return None

def solver_alt2(input_file):
    lines = read(input_file)
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    lines = read(input_file)
    words = 0
    count = lambda line, reflect=False: len(re.findall(r'XMAS', line if reflect else line[::-1]))
    count_board = lambda lines: sum([count(line) + count(line, reflect=True) for line in lines])
    
    words += count_board(lines)
    flipped = ["".join([l[i] for l in lines]) for i in range(len(lines[0]))]
    words += count_board(flipped)
    diag_left = diagonals(lines)
    words += count_board(diag_left)
    diag_right = diagonals(flipped[::-1])
    words += count_board(diag_right)
    return words

def solver2_alt3(input_file):
    lines = read(input_file)
    rows, cols = len(lines), len(lines[0])
    hit = lambda x, y: np.sum(x * y)
    board = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            board[r, c] = ord(lines[r][c])
    xmas = np.asarray([[77, 0, 83], [0, 65, 0], [77, 0, 83]])
    thresh = hit(xmas, xmas)
    Ys, Xs = np.where(board == 65)
    count = 0
    for y, x in zip(Ys, Xs):
        if x in (0, rows-1) or y in (0, cols-1):
            continue
        for mas in (xmas, xmas[:,::-1], xmas.T, xmas.T[::-1]):
            val = hit(mas, board[y-1:y+2, x-1:x+2])
            if val == thresh:
                count += 1
                break
    return count
