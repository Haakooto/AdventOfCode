import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time


def Intcode(array):
    pos = 0
    opcode = array[pos]
    while True:
        opcode = array[pos]
        if opcode == 1:
            array[array[pos + 3]] = array[array[pos + 1]] + array[array[pos + 2]]
        elif opcode == 2:
            array[array[pos + 3]] = array[array[pos + 1]] * array[array[pos + 2]]
        elif opcode == 99:
            break

        else:
            print("Something is wrong")
            print(array)
            sys.exit()
        pos += 4
    return array


def brute_force(program, verb, noun, target):
    for v in range(verb):
        for n in range(noun):
            instance = program.copy()
            instance[1] = n
            instance[2] = v

            res = Intcode(instance)
            if res[0] == target:
                return 100 * n + v


def test():
    a = np.array([1, 0, 0, 0, 99])
    b = np.array([2, 3, 0, 3, 99])
    c = np.array([2, 4, 4, 5, 99, 0])
    d = np.array([1, 1, 1, 4, 99, 5, 6, 0, 99])

    print(Intcode(a))
    print(Intcode(b))
    print(Intcode(c))
    print(Intcode(d))


def main():
    file = open("/home/hakon/Downloads/aoc2.txt", "r")
    program = file.readline().split(",")
    file.close()
    program = [int(i) for i in program]
    program = np.asarray(program)
    program2 = program.copy()

    program[1] = 12
    program[2] = 2

    result = Intcode(program)
    print(result[0])

    print(brute_force(program2, 99, 99, 19690720))


if __name__ == "__main__":
    main()
