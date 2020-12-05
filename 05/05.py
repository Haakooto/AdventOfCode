import numpy as np

def seatID(seat):
    col = seat[-3:].replace("L", "0").replace("R", "1")
    row = seat[:-3].replace("F", "0").replace("B", "1")
    row = sum([int(i) * 2 ** j for j, i in enumerate(row[::-1])])
    col = sum([int(i) * 2 ** j for j, i in enumerate(col[::-1])])
    ID = row * 8 + col
    return ID

maxID = 0
ids = np.arange(1033)
seats = []
with open("data.txt", "r") as file:
    for line in file.read().split("\n"):
        seat = seatID(line)
        seats.append(seat)
        if seat > maxID:
            maxID = seat
print(maxID)
free = np.asarray([i for i in ids if i not in seats])
your = free[np.where(np.gradient(free) != 1)[0][1]]
print(your)