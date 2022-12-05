from collections import Counter
rucksacks = open("input", "r").read().strip().split("\n")


priority = {}
for char in range(97, 97 + 26):
    priority[chr(char)] = char - 96
for char in range(65, 65 + 26):
    priority[chr(char)] = char - 64 + 26

S = 0

for sack in rucksacks:
    L = int(len(sack) / 2)
    c1, c2 = set(sack[:L]), set(sack[L:])
    double = list(c1 & c2)[0]

    S += priority[double]

print(S)
badges = 0

for sacks in range(0, len(rucksacks), 3):
    group = set(rucksacks[sacks])
    group &= set(rucksacks[sacks + 1])
    group &= set(rucksacks[sacks + 2])
    item = list(group)[0]
    badges += priority[item]

print(badges)