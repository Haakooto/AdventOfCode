import re
import numpy as np
from contextlib import contextmanager


def read(file):
    with open(file, "r") as file:
        house, ops = file.read().split("\n\n")
    return house.split("\n"), "".join(ops.split("\n"))

@contextmanager
def flip(house, op):
    rot = {">": 0, "v": 1, "<": 2, "^": 3}
    house = np.rot90(house, k=rot[op])
    try:
        yield house
    finally:
        house = np.rot90(house, k=-rot[op])

def move_right(house):
    y, x = np.where(house == np.inf)
    y, x = y[0], x[0]
    out = house[y, x+1:]
    block = np.where(out == -np.inf)[0][0]
    out = out[:block]
    if len(out):
        try:
            space = np.where(out == 0)[0][0] + 1
        except IndexError:
            pass
        else:
            xx = x + 1
            house[y, xx:xx+space] = house[y, x:x+space]
            house[y, x] = 0

def find_front(house, pts):
    new = []
    boxes = False
    for y, x, val in pts[-1]:
        if val in [-np.inf, 0]:
            continue
        c = house[y, x+1]
        new.append((y,x+1,c))
        if c not in [-np.inf, 0]:
            boxes = True
            if house[y+1, x+1] == c:
                new.append((y+1,x+1,c))
            else:
                new.append((y-1,x+1,c))
        if c == -np.inf:
            return pts, False

    pts.append(set(new))
    if boxes:
        return find_front(house, pts)
    return pts, True

def move_right_2(house):
    y, x = np.where(house == np.inf)
    y, x = y[0], x[0]
    if house[y, x+1] == -np.inf:
        return
    elif house[y, x+1] == 0:
        house[y, x+1] = np.inf
        house[y, x] = 0
        return
    
    cone, free = find_front(house, [[(y, x, house[y, x]),],])
    if free:
        for row in reversed(cone[:-1]):
            for y, x, c in row:
                if c != 0:
                    house[y, x  ] = 0
                    house[y, x+1] = c

def solver1_alt3(input_file):
    house, ops = read(input_file)
    rows, cols = len(house), len(house[0])
    warehouse = np.zeros((rows, cols))
    conv = {"#": -np.inf, ".": 0, "O": 1, "@": np.inf}

    for r in range(rows):
        for c in range(cols):
            warehouse[r, c] = conv[house[r][c]]
    
    for op in ops:
        with flip(warehouse, op) as house:
            move_right(house)
    
    Xs, Ys = np.where(warehouse == 1)
    gps = np.sum(Xs * 100 + Ys)
    return gps

def display(mat):
    def conv(r):
        if r == np.inf:
            return "@"
        elif r == -np.inf:
            return "#"
        elif r == 0:
            return "."
        else:
            return int(r)
    rows = "\n".join([" ".join([f'{conv(r):>3}' for r in row]) for row in mat])
    print(rows)

def solver2_alt3(input_file):
    house, ops = read(input_file)
    house = [
            row.replace("#", "##")
               .replace("O", "[]")
               .replace(".", "..")
               .replace("@", "@.") 
            for row in house
            ]
    rows, cols = len(house), len(house[0])
    warehouse = np.zeros((rows, cols))
    conv = {"#": -np.inf, ".": 0, "@": np.inf, "[": -1}

    box_count = 0
    for r in range(rows):
        for c in range(cols):
            if house[r][c] == "]":
                box_count += 1
                warehouse[r, c] = box_count
                warehouse[r, c-1] = box_count
            else:
                warehouse[r, c] = conv[house[r][c]]
    
    for i, op in enumerate(ops):
        with flip(warehouse, op) as house:
            if op in [">", "<"]:
                move_right(house)
            else:
                move_right_2(house)
    gps = 0
    for box in range(box_count):
        x, y = np.where(warehouse == box+1)
        gps += x[0] * 100 + y[0]
    return gps
