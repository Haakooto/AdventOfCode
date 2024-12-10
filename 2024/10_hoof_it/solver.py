import re
import numpy as np

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def walk(map, pos, part2=False):
    directions = np.array([[0, 0], [0,-1], [0, 1], [-1, 0], [1, 0]])
    see = directions[:, None, :] + pos
    heights = map[*see.T]
    valid = (heights - heights[:, :1]) == 1
    locs = see[valid.T]
    if part2:
        return locs
    return np.unique(locs, axis=0)

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    rows, cols = len(lines), len(lines[0])
    typography = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            typography[r, c] = int(lines[r][c])
    typography = np.pad(typography, 1, constant_values=-1)
    
    heads = np.asarray(np.where(typography == 0))
            
    score = 0
    for pos in heads.T:
        for _ in range(9):
            pos = walk(typography, pos, part2)
        score += pos.shape[0]
    return score

def solver_alt2(input_file):
    lines = read(input_file)
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    lines = read(input_file)
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    lines = read(input_file)
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
