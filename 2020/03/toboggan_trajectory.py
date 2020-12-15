import numpy as np

area = np.loadtxt("data.txt", dtype=int, converters={0: lambda s: list(s)}, comments=None)
area = np.where(area == 46, 0, 1)

max = area.shape[1]
slopes = ((1,1), (1,3), (1,5), (1,7), (2, 1))
total = 1

for y, x in slopes:
    N = area.shape[0] // y
    X = np.arange(0, N * x, x) % max
    Y = np.arange(0, N * y, y)
    trees = sum(area[Y, X])
    if x == 3:
        print(trees)
    total *= trees
print(total)