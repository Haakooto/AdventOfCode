import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time


def main():
    file = open("/home/hakon/Downloads/aoc1.txt", "r")

    masses = file.readlines()
    file.close()

    supertotal = 0
    for mass in masses:
        mod_tot = 0
        mass = int(mass.strip())
        fuel = mass
        while fuel > 0:
            fuel = max(np.floor(fuel / 3) - 2, 0)
            mod_tot += fuel

        supertotal += mod_tot

    print(f"Total: {supertotal}")


if __name__ == "__main__":
    main()
