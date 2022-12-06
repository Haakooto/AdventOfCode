msg = open("input", "r").read().strip()
for idx0 in (4, 14):
    idx = idx0
    while len(set(msg[idx-idx0:idx])) != idx0:
        idx += 1
    print(idx)