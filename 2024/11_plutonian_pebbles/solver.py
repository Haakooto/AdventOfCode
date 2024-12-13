import re
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

def read(file):
    with open(file, "r") as file:
        return [int(i) for i in re.findall(r'\d+', file.read())]

def solver_alt1(input_file, blinks, part2=False):
    if part2:
        blinks *= 3
    stones = read(input_file)
    line = defaultdict(lambda: 0)
    # line = Counter()
    for stone in stones:
        line[stone] += 1
    scount = [sum(line.values()),]
    ucount = [len(line)]
    for blink in range(blinks):
        new_line = defaultdict(lambda: 0)
        # new_line = Counter()
        for val, count in line.items():
            new = None
            if val == 0:
                val = 1
            elif (l:=len(s:=str(val))) % 2 == 0:
                val = int(s[:l//2])
                new = int(s[l//2:])
                new_line[new] += count
            else:
                val *= 2024
            new_line[val] += count
        line = new_line
        scount.append(sum(line.values()))
        ucount.append(len(line))

    fig, ax1 = plt.subplots()
    ax1.plot(scount, color="blue", label="Total count")
    ax2 = plt.twinx()
    ax2.plot(ucount, color="red", label="Unique count")
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    plt.legend(handles1 + handles2, labels1 + labels2)
    ax1.semilogy()
    ax2.semilogy()
    plt.grid()
    plt.savefig("stones.png")
    plt.clf()
    return sum(line.values())

