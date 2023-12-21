import numpy as np
import matplotlib.pyplot as plt


def parse(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    input = input[1:-1]
    i, c = input[1:-1], input[-1]
    c = {"0": "R", "1": "D", "2": "L", "3": "U"}[c]
    return c, int(i, 16)

def up(pos, dist=1):
    return pos[0], pos[1] - dist


def down(pos, dist=1):
    return pos[0], pos[1] + dist


def left(pos, dist=1):
    return pos[0] - dist, pos[1]


def right(pos, dist=1):
    return pos[0] + dist, pos[1]


dirs = {"U": up, "D": down, "L": left, "R": right}


def solver_alt2(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that behaves differently depending on part2
    return None, None


def solver_alt1(input_file, part2=False):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    start = (0, 0)
    pit = [start]
    boundary_length = 0
    for dig in lines:
        dir, cnt, color = dig.split()
        if part2:
            dir, cnt = parse(color)
        else:
            cnt = int(cnt)
        pit.append(dirs[dir](pit[-1], cnt))
        boundary_length += cnt

    # Using shoelace formula to calculate area, 
    #    as the sum of determinants of two and two consecutive points
    #    2A = |sum of determinants|
    # Then using Picks theorem to calculate the number of points inside the polygon
    #    A = I + B/2 - 1
    # Answer I want is I + B, so (2A + B + 2) / 2

    area = 0
    for i in range(len(pit)-1):
        area += pit[i][0]*pit[i+1][1] - pit[i+1][0]*pit[i][1]
    return (abs(area) + boundary_length + 2) // 2


def solver1_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part1. Used in conjunction with solver2_alt3
    return None


def solver2_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
