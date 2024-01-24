class Part:
    def __init__(self, line):
        x, m, a, s = line[1:-1].split(",")
        self.x = int(x.split("=")[1])
        self.m = int(m.split("=")[1])
        self.a = int(a.split("=")[1])
        self.s = int(s.split("=")[1])
        self.sum = self.x + self.m + self.a + self.s
    
class Rule:
    def __init__(self, wfs):
        self.conds = {}
        for wf in wfs.split(","):
            if ":" in wf:
                cond, ret = wf.split(":")
                self.conds[cond] = ret
            else:
                self.final = wf

    def __call__(self, part):
        for cond, ret in self.conds.items():
            if eval(f"part.{cond}"):
                return ret
        return self.final
         
def parse_input(input_file):
    with open(input_file, "r") as file:
        rules, parts = file.read().split("\n\n")
    return rules.split("\n"), parts.split("\n")[:-1]

def build(rules, part2=False):
    parsed_rules = {}
    for rule in rules:
        name, wfs = rule.split("{")
        if part2:
            parsed_rules[name] = wfs[:-1].split(",")
        else:
            parsed_rules[name] = Rule(wfs[:-1])
    return parsed_rules

def accept(rules, part):
    rule = rules["in"]
    while True:
        reply = rule(part)
        if reply == "A":
            return True
        elif reply == "R":
            return False
        rule = rules[reply]

def solver1_alt3(input_file):
    rules, parts = parse_input(input_file)
    rules = build(rules)
    sum = 0
    for part in parts:
        part = Part(part)
        if accept(rules, part):
            sum += part.sum
    return sum

# ? Part 2
from functools import reduce
from operator import mul

def sum_range(ranges):
    def number_of_combinations(range_tuple):
        a, b = range_tuple
        return b - a + 1
    # Lol first spent a lot of time getting the actual sum of all combinations
    # After a lot of trial and error, and with the help of ChatGPT, I got this solution
    # It works great and is very fast
    # However, it is not was was asked for in the problem and therefore useless
    # Though I'm keeping it here for posterity, as it was a much harder problem than the actual one
    total_combinations = reduce(mul, (number_of_combinations(value) for value in ranges.values()))
    average_sum = sum((b + a) / 2.0 for a, b in ranges.values())
    result = int(total_combinations * average_sum)
    return result

def sum_range_len(ranges):
        # The true solution,
        # just count the number of combinarions, not their actual sums
        i = 1
        for low, high in ranges.values():
            i *= high - low + 1
        return i

def split(ranges, name, rule_registry):
        if name == "A":
            return sum_range_len(ranges)
        elif name == "R":
            return 0
        if len(rule_registry[name]) == 1:  # If only one workflow left and is not A or R, apply new rule
            return split(ranges, rule_registry[name][0], rule_registry)
        
        workflow = rule_registry[name].pop(0)
        condition, new_rule = workflow.split(":")
        type = condition[0]
        dir = condition[1]
        val = int(condition[2:])
        left = ranges.copy()
        right = ranges.copy()
        if dir == ">":
            left[type] = (val+1, left[type][1])
            right[type] = (right[type][0], val)
        else:
            left[type] = (left[type][0], val-1)
            right[type] = (val, right[type][1])
        l = split(left, new_rule, rule_registry)
        r = split(right, name, rule_registry)
        return l + r

def solver2_alt3(input_file):
    rules, _ = parse_input(input_file)
    rules = build(rules, part2=True)
    all_possible = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    count = split(all_possible, "in", rules)
    return count
