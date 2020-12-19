import re

ruls, msgs = open("input").read().strip().split("\n\n")

rules = {}
for rule in ruls.splitlines():
    num, rest = rule.split(": ")
    rules[int(num)] = rest

def get_regex(num):
    if num in regexs:
        return regexs[num]

    regex = to_regex(rules[num])
    regexs[num] = regex
    return regex

def to_regex(rule):
    if rule in ("a", "b"):
        return rule

    return "(" + ")|(".join(["(" + ")(".join([get_regex(int(i)) for i in option.split(" ")]) + ")" for option in rule.split(" | ")]) + ")"

regexs = {}
regex0 = get_regex(0)

matches = sum([bool(re.fullmatch(regex0, msg)) for msg in msgs.splitlines()])
print(matches)
