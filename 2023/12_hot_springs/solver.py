import re

def parse(springs, part2=False):
    springs, groups = springs.split(" ")
    springs = "?".join([springs for _ in range(1 + 4 * part2)])
    groups = tuple([int(x) for x in groups.split(",")] * (1 + 4 * part2))
    return springs, groups

def arragements(springs, groups, cache={}):
    if len(groups) == 0:
        cache[(springs, groups)] = int("#" not in springs)
    elif len(springs) < sum(groups) + len(groups) - 1:
        cache[(springs, groups)] = 0
    if (springs, groups) in cache:
        return cache[(springs, groups)]
    
    perms = 0
    if "." not in springs[:groups[0]] and (springs + ".")[groups[0]] != "#":
        perms += arragements(springs[groups[0]+1:], groups[1:], cache=cache)
    if springs[0] != "#":
        perms += arragements(springs[1:], groups, cache=cache)
    cache[(springs, groups)] = perms
    return perms

def solver_alt1(input_file, part2=False):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    cache = {}
    perms = 0
    for line in lines:
        springs, groups = parse(line, part2=part2)
        springs = re.sub(r'(?:^\.+)|(?:\.+$)|(\.)\1+', r'\1', springs)  # Remove all but one dot in a row
        a = arragements(springs, groups, cache=cache)
        perms += a
    return perms
    # One function that behaves differently depending on part2

def solver_alt2(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
