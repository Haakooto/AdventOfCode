carries = []
with open("input", "r") as file:
    elves = file.read().split("\n\n")
    for elf in elves:
        carries.append(sum([int(i) for i in elf.split()]))

print(max(carries))
print(sum([carries.pop(carries.index(max(carries))) for _ in range(3)]))