import re

def func_that_does_the_thing(levels, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    diffs = [a - b for a, b in zip(levels[1:], levels[:-1])]
    if 0 in diffs:
        return False
    if abs(max(diffs, key=abs)) > 3:
        return False
    signs = sum([i > 0 for i in diffs])
    if signs not in (0, len(diffs)):
        return False
    return True

def solver_alt1(input_file, part2=False):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that behaves differently depending on part2
    return None

def solver_alt2(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part1. Used in conjunction with solver2_alt3
    safe = 0
    for report in lines:
        levels = [int(i) for i in re.findall(r"(\d+)", report)]
        safe += func_that_does_the_thing(levels)
    return safe

def solver2_alt3(input_file):
    with open(input_file, "r") as file:
        lines = file.read().split("\n")[:-1]  # Most typical case
    # One function that does part2. Used in conjunction with solver1_alt3
    safe = 0
    for report in lines:
        levels = [int(i) for i in re.findall(r"(\d+)", report)]
        if func_that_does_the_thing(levels, part2=False):
            safe += 1
            continue
        for index in range(len(levels)):
            _levels = levels[:index] + levels[index+1:]
            if func_that_does_the_thing(_levels, part2=True):
                safe += 1
                break

    return safe
