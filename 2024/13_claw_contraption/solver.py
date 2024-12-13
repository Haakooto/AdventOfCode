import re
import numpy as np

def parse(file):
    with open(file, "r") as file:
        lines = file.read().strip().split("\n\n")
    nums = [re.findall(r'\d+', line) for line in lines]
    return [[int(i) for i in line] for line in nums]

def integer_close(x, tol=1e-9):
    return abs(x - round(x)) < tol

def all_integers(vec, tol=1e-9):
    return all(integer_close(v, tol) for v in vec)

def play(input, part2=False):
    AB = np.array(input[:4]).reshape((2,2))
    XY = np.array(input[4:])
    if part2:
        XY += 10000000000000

    costs = np.array([3, 1])
    inv = np.linalg.inv(AB)
    count = XY @ inv
    valid = all_integers(count, 1e-4)
    cost = costs.dot(count)
    if valid:
        return cost
    return 0

def solver_alt1(input_file, part2=False):
    games = parse(input_file)
    total = 0
    for game in games:
        c = play(game, part2=part2)
        total += c
    return total

def solver_alt2(input_file):
    lines = parse(input_file)
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    lines = parse(input_file)
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    lines = parse(input_file)
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
