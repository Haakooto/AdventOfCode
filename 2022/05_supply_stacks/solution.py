import numpy as np
from copy import deepcopy

stacks, cmds = open("input", "r").read().split("\n\n", 1)
stacks = np.asarray([s for s in stacks])[-2::-4].reshape(-1, 9).T[::-1]
stacks = {stack[0]: [s for s in stack[1:] if s != " "] for stack in stacks}
cmds = cmds.strip().split("\n")

stacks_one = deepcopy(stacks)
stacks_two = deepcopy(stacks)

for cmd in cmds:
    cnt, source, target = cmd.split(" ")[1::2]
    tmp = []
    for _ in range(int(cnt)):
        stacks_one[target].append(stacks_one[source].pop())
        tmp.append(stacks_two[source].pop())
    for _ in range(int(cnt)):
        stacks_two[target].append(tmp.pop())

print("".join([v[-1] for v in stacks_one.values()]))
print("".join([v[-1] for v in stacks_two.values()]))
