import numpy as np

crabs = np.asarray([int(i) for i in open("08").read().strip().split(",")])
centre = int(np.median(crabs))
print(sum(abs(crabs - centre)))


min = np.inf
for centre in np.arange(max(crabs)):
    N = abs(crabs - centre)
    fuel = sum(N * (N + 1) / 2)
    if fuel < min:
        min = fuel
print(int(min))
