pairs = open("input", "r").read().strip().split("\n")

covers = 0
overlaps = 0

for pair in pairs:
    a, b = pair.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    ranges = [[int(a1), int(a2)], [int(b1), int(b2)]]

    if ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]:
        covers += 1
    elif ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
        covers += 1

    if ranges[0][1] >= ranges[1][0] and ranges[0][0] <= ranges[1][1]:
        overlaps += 1

print(covers)
print(overlaps)
