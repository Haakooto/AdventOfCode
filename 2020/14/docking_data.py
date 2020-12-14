from itertools import permutations as per, combinations_with_replacement as comwr
mem = {}

for line in open("i").read().strip().splitlines():
    op, val = line.split(" = ")
    if op == "mask":
        mask = [i for i in val]
    else:
        adress = op[4:-1]
        bit = [i for i in f"{int(val):b}".zfill(36)]
        value = ""
        for m, b in zip(mask, bit):
            if m == "X":
                value += b
            else:
                value += m
        mem[adress] = int(value, 2)
print(sum(list(mem.values())))


mem = {}
for line in open("i").read().strip().splitlines():
    op, val = line.split(" = ")
    if op == "mask":
        mask = [i for i in val]
    else:
        adress = [i for i in f"{int(op[4:-1]):b}".zfill(36)]
        new = ""
        for m, a in zip(mask, adress):
            if m == "0":
                new += a
            else:
                new += m
        perms = set()
        for com in comwr((0, 1), new.count("X")):
            for perm in per(com):
                perms.add(perm)
        for perm in perms:
            tmp = new
            for i in perm:
                tmp = tmp.replace("X", str(i), 1)
            mem[int(tmp, 2)] = int(val)
print(sum(list(mem.values())))
