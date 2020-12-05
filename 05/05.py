import numpy as np

maxID = 0
ids = np.arange(1033)
seats = []
with open("data.txt", "r") as file:
    for line in file.read().split("\n"):
        seat = sum([int(i) * 2 ** j for j, i in enumerate(line.replace("L", "0").replace("R", "1").replace("F", "0").replace("B", "1")[::-1])])
        seats.append(seat)
        if seat > maxID:
            maxID = seat
print(maxID)
free = np.asarray([i for i in ids if i not in seats])
your = free[np.where(np.gradient(free) != 1)[0][1]]
print(your)