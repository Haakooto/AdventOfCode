from collections import Counter

fish = [int(i) for i in open("input", "r").read().strip().split(",")]
counter = [0]*7
younglings = [0]*2
for f in fish:
    counter[f] += 1

for day in range(256):
    born = counter[0]
    counter[0:-1] = counter[1:]
    counter[-1] = younglings[0] + born
    younglings[0] = younglings[1]
    younglings[1] = born

print(sum(counter) + sum(younglings))