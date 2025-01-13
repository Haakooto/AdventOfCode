import re
from tqdm import tqdm
from functools import cache

def read(file):
    with open(file, "r") as file:
        towels, designs = file.read().split("\n\n")
    return towels.split(", "), designs.split("\n")[:-1]

def check_if_possible(spans, start, end):
    for i, (span, s) in enumerate(spans):
        if span[0] == start:
            if span[1] == end:
                return True
            for j, (other, q) in enumerate(spans[i+1:]):
                if other[0] == span[1]:
                    if check_if_possible(spans[j+1:], span[1], end):
                        return True
    return False

@cache
def count_all_possible(spans, start, end):
    c = 0
    for i, (span, s) in enumerate(spans):
        if span[0] == start:
            if span[1] == end:
                c += 1
            for j, (other, q) in enumerate(spans[i+1:]):
                if other[0] == span[1]:
                    c += count_all_possible(spans[j+1:], span[1], end)
    return c

def solver_alt2_old(input_file):
    towels, designs = read(input_file)
    possible = 0
    unique = 0
    for design in designs:
        spans = []
        for towel in towels:
            spans.extend([(m.span(), m.group()) for m in re.finditer(towel, design)])
        spans = tuple(sorted(spans, key=lambda x: x[0][0]))
        c = count_all_possible(spans, 0, len(design))
        unique += c
        if c:
            possible += 1
    return possible, unique

@cache
def stack(design, towels):
    c = 0
    p = []
    if len(design) == 0:
        return True, []
    for i, (t, s) in enumerate(towels):
        if design[:s] == t:
            v, c = stack(design[s:], towels)
            if v:
                p.extend(t)
    return c, p

def solver_alt2_old2(input_file):
    towels, designs = read(input_file)
    possible = 0
    unique = 0
    towels = tuple((t, len(t)) for t in towels)
    for design in designs:
        if stack(design, towels):
            possible += 1
    return possible, unique

def count_matches(s, substrings, start=0, depth=0):
    if start == len(s):
        return 1

    count = 0
    iterator = tqdm(substrings, leave=False, desc=f"depth: {depth}") if depth < 10 else substrings
    for sub in iterator:
        if s.startswith(sub, start):
            count += count_matches(s, substrings, start + len(sub), depth+1)
    return count

def solver_alt2(input_file):
    towels, designs = read(input_file)
    possible = 0
    unique = 0
    for d in tqdm(designs):
        count = count_matches(d, towels)
        if count:
            possible += 1
        unique += count
    return possible, unique
