import numpy as np
rules, your, nearby = open("input").read().strip().split("\n\n")
your = [int(i) for i in your.splitlines()[1].split(",")]

ticket_rules = {}
for line in rules.splitlines():
    field, vals = line.split(": ")
    v1, v2 = vals.split(" or ")
    a, b = v1.split("-")
    c, d = v2.split("-")
    ticket_rules[field] = [i for i in range(int(a), int(d) + 1) if i not in range(int(b) + 1, int(c))]

tsre = 0
valids = []
for ticket in nearby.splitlines()[1:]:
    invalid = False
    for val in ticket.split(","):
        valid = [int(val) in rule for rule in ticket_rules.values()]
        if not sum(valid):
            tsre += int(val)
            invalid = True
    if not invalid:
        valids.append(ticket)
print(tsre)

valid = {field: np.zeros(len(your)) for field in ticket_rules}
for ticket in valids:
    ticket = [int(i) for i in ticket.split(",")]
    for field in ticket_rules:
        valid[field] += [int(val in ticket_rules[field]) for val in ticket]
for field in valid:
    valid[field] = np.where(valid[field] == max(valid[field]))[0]

determined = {}
while len(determined) < len(your):
    for field in valid:
        if len(valid[field]) == 1:
            idx = int(valid[field][0])
            determined[field] = idx
            for f in valid:
                valid[f] = [i for i in valid[f] if i != idx]
idxs = [determined[f] for f in determined if "departure" in f]
deps = [your[i] for i in idxs]
print(np.prod(deps))