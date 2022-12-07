import numpy as np

def expand(region, world, cache):
    if cache == region:
        return region

    permutes = [np.asarray(n) for n in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    new_points = set()

    for point in (region - cache):
        n = np.asarray(point)
        for p in permutes:
            q = n + p
            if world[q[0], q[1]] != 9:
                new_points |= set((tuple(n+p),))
    cache |= region
    region |= new_points
    return expand(region, world, cache)


floor = np.pad(np.loadtxt("input", dtype=int, converters={0: lambda s: [i - 48 for i in s]}, ndmin=2), 1,  'constant', constant_values=9)
low_sum = 0
basins = []
N, M = floor.shape
for x in range(1, N-1):
    for y in range(1, M-1):
        local = [floor[x, y], floor[x+1, y], floor[x-1, y], floor[x, y+1], floor[x, y-1]]
        if local[0] == min(local) and local[0] != 9:
            low_sum += 1 + local[0]
            basins.append(len(expand(set(((x, y),)), floor, set())))

print(low_sum)
print(np.prod(sorted(basins)[-3:]))