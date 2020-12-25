import numpy as np

lines = open("test").read().splitlines()
time = int(lines[0])
all_shuttles = np.array([(j, i) for j, i in enumerate(lines[1].split(","))])
all_shuttles = np.array(
    [(int(j) % int(i), int(i)) for j, i in all_shuttles if i != "x"]
)
a, shuttles = all_shuttles.T
time_to_next = shuttles - time % shuttles
first = np.argmin(time_to_next)
print(shuttles[first] * time_to_next[first])


