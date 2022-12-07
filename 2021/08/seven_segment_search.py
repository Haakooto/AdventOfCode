counter = 0
sum = 0
for line in open("08").read().strip().split("\n"):
    # * initialise lists
    unique, output = line.split(" | ")
    uniques = ["".join(sorted(u)) for u in unique.split(" ")]
    outputs = ["".join(sorted(o)) for o in output.split(" ")]
    num_mapper = {}
    seg_mapper = {}

    # * identify 1, 4, 7 and 8
    while len(num_mapper) != 4:
        u = uniques.pop(0)
        if len(u) == 2:
            num_mapper[1] = u
        elif len(u) == 3:
            num_mapper[7] = u
        elif len(u) == 4:
            num_mapper[4] = u
        elif len(u) == 7:
            num_mapper[8] = u
        else:
            uniques.append(u)

    # * can now identify a
    seg_mapper["a"] = list(set(num_mapper[7]) - set(num_mapper[1]))[0]

    # * 0, 6 and 9 have 6 segments, and can with current info be found
    # * identifying 6 using 1 lets me find c
    # * identifying 0 using 4 and a lets me find d
    # * identifying 9 using 8 lets me find e
    while len(num_mapper) != 7:
        u = uniques.pop(0)
        if len(u) == 6:
            c_cand = list(set(num_mapper[1]) - set(u))
            if len(c_cand) != 0:
                num_mapper[6] = u
                seg_mapper["c"] = c_cand[0]
                continue
            g_cand = list(set(num_mapper[4]) - set(u) - set(seg_mapper["a"]))
            if len(g_cand) != 0:
                num_mapper[0] = u
                seg_mapper["d"] = g_cand[0]
                continue
            num_mapper[9] = u
            seg_mapper["e"] = list(set(num_mapper[8]) - set(u))[0]
        else:
            uniques.append(u)
    # * segments f, b and g can now be identified
    seg_mapper["f"] = list(set(num_mapper[1]) - set(seg_mapper["c"]))[0]
    seg_mapper["b"] = list(set(num_mapper[4]) - set([seg_mapper[i] for i in "cdf"]))[0]
    seg_mapper["g"] = list(set(num_mapper[8]) - set(seg_mapper.values()))[0]
    # * Now all segments are identified

    num_mapper[2] = "".join(sorted([seg_mapper[i] for i in "acdeg"]))
    num_mapper[3] = "".join(sorted([seg_mapper[i] for i in "acdfg"]))
    num_mapper[5] = "".join(sorted([seg_mapper[i] for i in "abdfg"]))

    # * we are done!
    rev_mapper = {v: k for k, v in num_mapper.items()}

    #* start parsing displays
    for out in outputs:
        n = rev_mapper[out]
        if n in [1, 4, 7, 8]:
            counter += 1

    sum += int("".join(str(rev_mapper[out]) for out in outputs))

print(counter)
print(sum)