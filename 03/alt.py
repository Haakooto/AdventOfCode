import numpy as np

area = np.loadtxt("data.txt", dtype=int, converters={0: lambda s: list(s)}, comments=None)
area = np.where(area == 46, 0, 1)

max = area.shape[1]
slopes = ((1,1), (1,3), (1,5), (1,7), (2, 1))
total = 1

for y, x in slopes:
    location = 0
    trees = 0
    for i in range(0, area.shape[0], y):
        trees += area[i, location]
        location += x
        location %= max
    if x == 3:
        print(trees)
    total *= trees
print(total)
