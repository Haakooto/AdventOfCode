import re

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]  # Most typical case

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    # One function that behaves differently depending on part2
    return None

def solver_alt2(input_file):
    lines = read(input_file)
    # One function that returns both part1 and part2
    return None, None

def solver1_alt3(input_file):
    lines = read(input_file)
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    lines = read(input_file)
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
