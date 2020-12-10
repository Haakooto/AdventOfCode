adapters = [0]
for i in open("i").read().splitlines():
    if i != "":
        adapters.append(int(i))
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
print(diffs.count(1) * diffs.count(3))

combs = {0:1, 1:1, 2:2, 3:4, 4:7}
count = combs[diffs.index(3)]
for i in range(len(diffs) - 1):
    if diffs[i] == 3:
        next = diffs[i + 1:].index(3)
        count *= combs[next]
print(count)
