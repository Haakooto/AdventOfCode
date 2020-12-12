import numpy as np

loc = np.array([0, 0])
wpt = np.array([10, 1])

rot = lambda s, x, y: np.array([x * np.cos(s) - np.sin(s) * y, np.sin(s) * x + np.cos(s) * y])

command = {"N": lambda v: (loc, wpt + np.array([0, v])),
           "S": lambda v: (loc, wpt - np.array([0, v])),
           "E": lambda v: (loc, wpt + np.array([v, 0])),
           "W": lambda v: (loc, wpt - np.array([v, 0])),
           "L": lambda v: (loc, rot(v * np.pi / 180, *wpt)),
           "R": lambda v: (loc, rot(-v * np.pi / 180, *wpt)),
           "F": lambda v: (loc + v * wpt, wpt)
           }

for line in open("i").read().splitlines():
    if line == "":
        continue
    act, val = line[0], int(line[1:])
    loc, wpt = command[act](val)

print(round(sum(abs(loc))))