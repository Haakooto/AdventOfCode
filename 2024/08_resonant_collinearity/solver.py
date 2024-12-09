import re
import numpy as np
from itertools import combinations

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def inside(p, s):
    # lazily assume square grid
    return max(p) < s and min(p) >= 0

def find_nodes(map, freq, part2=False):
    if part2:
        return find_nodes2(map, freq)
    size, _ = map.shape
    locs = np.asarray(np.where(map == freq))
    combs = combinations(range(locs.shape[1]), 2)
    nodes = []
    for a, b in combs:
        a, b = locs[:, a], locs[:, b]
        vec = b - a
        for p in (b + vec, a - vec):
            if inside(p, size):
                nodes.append(tuple(p))
    return set(nodes)

def find_nodes2(map, freq):
    size, _ = map.shape
    locs = np.asarray(np.where(map == freq))
    combs = combinations(range(locs.shape[1]), 2)
    nodes = []
    for a, b in combs:
        a, b = locs[:, a], locs[:, b]
        vec = b - a
        if max(vec) % min(vec) == 0 and 1 not in abs(vec):
            print("Turns out this was not an issue afterall")
            vec //= min(vec)
        i = -size  # worst possible case
        while not inside(node:= a + i * vec, size):
            i += 1
        while inside(node:= a + i * vec, size):
            nodes.append(tuple(node))
            i += 1
    return set(nodes)

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    rows, cols = len(lines), len(lines[0])
    map = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            map[r, c] = ord(lines[r][c])
    freqs = np.unique(map)[1:]
    nodes = set()
    for freq in freqs:
        nodes.update(find_nodes(map, freq, part2=part2))
    return len(nodes)
