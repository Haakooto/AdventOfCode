import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time


def index(wire):
    L = sum(I[1] for I in wire)
    print(L)
    idxs = np.zeros((L, 2))

    total = -1
    for cmd in wire:
        if cmd[0] == "R":
            change = np.array([1, 0])
        elif cmd[0] == "L":
            change = np.array([-1, 0])
        elif cmd[0] == "U":
            change = np.array([0, 1])
        elif cmd[0] == "D":
            change = np.array([0, -1])
            
        for i in range(cmd[1]):
            idxs[total + 1] = idxs[total] + change
            total += 1

    return idxs

def same(fir, sec):
    cross = np.zeros(2)
    for elem in fir:
        for suck in sec:
            if (elem == suck).all():
                cross = np.vstack((cross, elem))
    return np.min(np.sum(abs(cross[1:]), axis=1))

def same2(fir, sec):
    cross = np.zeros(2)
    for elem in fir:
        S = sec - elem
        S = np.sum(S, axis = 1)
        print(S)
        print(0 in S)
        sys.exit()

def test():
    w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    w3 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    w4 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

    for w1, w2 in ((w1, w2), (w3, w4)):
        w1 = [[c[0], int(c[1:])] for c in w1.split(",")]
        w2 = [[c[0], int(c[1:])] for c in w2.split(",")]
        
        i1 = index(w1)
        i2 = index(w2)
        D = same2(i1, i2)
        print(D)

def main():
    file = open("/home/hakon/Downloads/aoc3.txt", "r")
    wires = file.readlines()
    file.close()
    wire1, wire2 = wires
    wire1 = [[c[0], int(c[1:])] for c in wire1.split(",")]
    wire2 = [[c[0], int(c[1:])] for c in wire2.split(",")]

    i1 = index(wire1)
    i2 = index(wire2)
    D = same(i1, i2)
    print(D)


if __name__ == "__main__":
    test()
    # main()
