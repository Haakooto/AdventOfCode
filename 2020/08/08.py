def run_prog(codes):
    acc = 0
    loc = 0
    seen = []
    while loc not in seen:
        seen.append(loc)
        if codes[loc] == "":
            return acc, True

        op, arg = codes[loc].split(" ")
        if op == "acc":
            acc += int(arg)
            loc += 1
        elif op == "jmp":
            loc += int(arg)
        elif op == "nop":
            loc += 1

    return acc, False


codes = open("i").read().splitlines()
print(run_prog(codes)[0])

for from_cmd, to_cmd in (("jmp", "nop"), ("nop", "jmp")):
    for i, line in enumerate(codes):
        if from_cmd in line:
            new_codes = codes.copy()
            new_codes[i] = new_codes[i].replace(from_cmd, to_cmd)
            acc, terminated = run_prog(new_codes)
            if terminated:
                print(acc)