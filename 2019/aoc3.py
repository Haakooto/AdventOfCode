import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time

# np.set_printoptions(threshold=sys.maxsize)


def make_graph(wire, N=100):
    grid = np.zeros((N, N), dtype=bool)
    # start = np.array([int(N / 10), int(N / 10)])
    start = np.array([0, 0])
    current = start.copy()
    for dir, len in wire:
        if dir == "R":
            change = np.array([1, 0])
        elif dir == "L":
            change = np.array([-1, 0])
        elif dir == "U":
            change = np.array([0, 1])
        elif dir == "D":
            change = np.array([0, -1])

        for _ in range(len):
            try:
                grid[current[0], current[1]] += 1
                current += change
            except IndexError:
                return make_graph(wire, N * 2)
    return grid, N


def find_cross_dist(grid1, grid2, N1, N2):
    if N1 > N2:
        tmp = grid2.copy()
        grid2 = np.zeros((N1, N1))
        grid2[:N2, :N2] = tmp
    elif N1 < N2:
        tmp = grid1.copy()
        grid1 = np.zeros((N2, N2))
        grid1[:N1, :N1] = tmp
        
    diff = grid1 * 3 + grid2

    cross = np.asarray(np.where(diff == 4))
    dists = np.sort(np.sum(cross, axis=0))
    return dists


def test():
    w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    w3 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    w4 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

    for w1, w2 in ((w1, w2), (w3, w4)):
        w1 = [[c[0], int(c[1:])] for c in w1.split(",")]
        w2 = [[c[0], int(c[1:])] for c in w2.split(",")]
        g1, n1 = make_graph(w1)
        g2, n2 = make_graph(w2)
        D = find_cross_dist(g1, g2, n1, n2)
        print(D)


def main():
    file = open("/home/hakon/Downloads/aoc3.txt", "r")
    wires = file.readlines()
    file.close()
    wire1, wire2 = wires
    wire1 = [[c[0], int(c[1:])] for c in wire1.split(",")]
    wire2 = [[c[0], int(c[1:])] for c in wire2.split(",")]

    g1, n1 = make_graph(wire1)
    g2, n2 = make_graph(wire2)
    D = find_cross_dist(g1, g2, n1, n2)
    print(D)


if __name__ == "__main__":
    test()
    main()
