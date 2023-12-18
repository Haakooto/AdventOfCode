
def aoc_hash(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    current = 0
    for i in input:
        current += ord(i)
        current *= 17
        current %= 256
    return current

class Lens:
    def __init__(self, label, fl=-1):
        self.label = label
        self.fl = int(fl)
        self.hash = aoc_hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __add__(self, other):
        self.fl = other.fl

    def __repr__(self):
        return f"{self.label}={self.fl}"


def read(file):
    with open(file, "r") as f:
        lines = f.readline().strip().split(",")
    return lines

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver_alt2(input_file):
    lines = read(input_file)
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    sequence = read(input_file)
    sum = 0
    for step in sequence:
        sum += aoc_hash(step)
    # One function that behaves differently depending on part2
    return sum

def solver2_alt3(input_file):
    sequence = read(input_file)
    boxes = {i: [] for i in range(256)}
    for step in sequence:
        if "=" in step:
            L = Lens(*step.split("="))
            lenses = boxes[L.hash]
            if L in lenses:
                lenses[lenses.index(L)] = L
            else:
                lenses.append(L)
        else:
            L = Lens(step[:-1], -1)
            if L in boxes[L.hash]:
                boxes[L.hash].remove(L)
    value = 0
    for i, box in boxes.items():
        for ii, lens in enumerate(box):
            value += (i + 1) * (ii + 1) * lens.fl
    # One function that does part2. Used in conjunction with solver1_alt3
    return value
