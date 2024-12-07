import re
from collections import defaultdict

def read(file):
    with open(file, "r") as file:
        return file.read()

def parse_rules(rules):
    X = defaultdict(lambda: [])
    Y = defaultdict(lambda: [])
    nums = [int(i) for i in re.findall(r'\d+', rules)]
    for x, y in zip(nums[::2], nums[1::2]):
        X[x].append(y)
        Y[y].append(x)
    return X, Y

def parse_queue(queue):
    queues = []
    for q in queue.split("\n")[:-1]:
        queues.append([int(i) for i in re.findall(r'\d+', q)])
    return queues

def valid(queue, rules):
    for i, p in enumerate(queue[::-1]):
        if p in rules.keys():
            rest = set(queue[:-i-1])
            if rest.intersection(rules[p]):
                return False
    return True

def fix(queue, rules):
    for i, p in enumerate(queue):
        behind = set(queue[i+1:]).intersection(rules[p])
        if behind:
            v = queue.pop(i)
            idx = max([queue.index(b) for b in behind])
            queue.insert(idx+1, v)
    return queue

def func_that_does_the_thing(input, part2=False):
    # Do the thing. For when the input is a list of inputs treated separately
    return None

def solver_alt1(input_file, part2=False):
    lines = read(input_file)
    # One function that behaves differently depending on part2
    return None

def solver_alt2(input_file):
    lines = read(input_file)
    rules, queue = lines.split("\n\n")
    XtoY, YtoX = parse_rules(rules)
    
    queues = parse_queue(queue)
    sum1 = 0
    sum2 = 0
    for queue in queues:
        changed = False
        while not valid(queue, XtoY):
            changed=True
            queue = fix(queue, YtoX)
        val = queue[len(queue)//2]
        if changed:
            sum2 += val
        else:
            sum1 += val
    return sum1, sum2

def solver1_alt3(input_file):
    lines = read(input_file)
    # One function that does part1. Used in conjunction with solver2_alt3
    return None

def solver2_alt3(input_file):
    lines = read(input_file)
    # One function that does part2. Used in conjunction with solver1_alt3
    return None
