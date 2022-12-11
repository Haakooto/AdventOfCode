import numpy as np

forest = np.loadtxt("input", dtype=int, converters={0: lambda s: [i - 48 for i in s]}, ndmin=2)
N, M = forest.shape
visible = 2 * N + 2 * M - 4
max_sight = 0

for i in range(1, N-1):
    for j in range(1, M-1):
        vis = False
        sight = 1
        for line in (forest[i:N, j], forest[:i+1, j][::-1], forest[i, j:N], forest[i, :j+1][::-1]):
            sight_line = line[0] <= line[1:]
            try:
                sight *= np.where(sight_line)[0][0] + 1
            except IndexError:
                sight *= len(line) - 1
                vis = True
        visible += vis
        max_sight = max(max_sight, sight)

print(visible)
print(max_sight)

