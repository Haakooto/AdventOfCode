import numpy as np

dir = 0
loc = np.array([0, 0])

command = {"N": lambda v: (loc + np.array([0, v]), dir),
           "S": lambda v: (loc - np.array([0, v]), dir),
           "E": lambda v: (loc + np.array([v, 0]), dir),
           "W": lambda v: (loc - np.array([v, 0]), dir),
           "L": lambda v: (loc, dir + v),
           "R": lambda v: (loc, dir - v),
           "F": lambda v: (loc + v * np.array([np.cos(dir * np.pi / 180), np.sin(dir * np.pi / 180)]), dir)
           }

for line in open("i").read().splitlines():
    if line == "":
        continue
    act, val = line[0], int(line[1:])
    loc, dir = command[act](val)

print(sum(abs(loc)))

