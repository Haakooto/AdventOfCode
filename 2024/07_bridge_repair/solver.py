import re
from math import log10 as log, floor

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def parse(line):
    return [int(i) for i in re.findall(r'\d+', line)]

def concat(a, b):
    digits = floor(log(b)) + 1
    c = a * 10 ** digits + b
    return c

def valid(result, equation, part2=False):
    if len(equation) == 1:
        return result == equation[0]
    a = equation.pop(0)
    for op in ops:
        new_eq = equation.copy()
        new_eq[0] = op(a, new_eq[0])
        if valid(result, new_eq, part2):
            return True
    return False


def solver_alt1(input_file, part2=False):
    global ops 
    ops = [lambda a, b: a + b, lambda a, b: a * b]
    if part2:
        ops += [concat]
        
    lines = read(input_file)
    sum = 0
    for line in lines:
        result, *nums = parse(line)
        if valid(result, nums, part2=part2):
            sum += result
    return sum
