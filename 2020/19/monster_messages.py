import re

ruls, msgs = open("inputs19").read().strip().split("\n\n")

rules = {}
for rule in ruls.splitlines():
    num, rest = rule.split(": ")
    rules[int(num)] = rest

def get_regex(num, level=0):
    if level > 20:
        return "x"
    if num in regexs:
        return regexs[num]

    regex = to_regex(rules[num], level)
    regexs[num] = regex
    return regex

def to_regex(rule, lev):
    if rule in ("a", "b"):
        return rule

    return "(" + ")|(".join(["(" + ")(".join([get_regex(int(i), lev+1) for i in option.split(" ")]) + ")" for option in rule.split(" | ")]) + ")"

regexs = {}
regex0 = get_regex(0)

matches = sum([bool(re.fullmatch(regex0, msg)) for msg in msgs.splitlines()])
print(matches)


changes = "8: 42 | 42 8\n11: 42 31 | 42 11 31"
for chang in changes.split("\n"):
    num, rest = chang.split(": ")
    rules[int(num)] = rest

regexs = {}
regex0 = get_regex(0)

matches = sum([bool(re.fullmatch(regex0, msg)) for msg in msgs.splitlines()])
print(matches)