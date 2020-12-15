import numpy as np
from itertools import permutations
nums = np.loadtxt("i", dtype=int, delimiter="\n")
pream = 25
idx = pream


while nums[idx] in [sum(i) for i in list(permutations(nums[idx - pream: idx], 2))]:
    idx += 1
num1 = nums[idx]
print(num1)

for set_len in range(2, len(nums)):
    for i in range(0, len(nums) - set_len):
        cont = nums[i: i + set_len]
        if sum(cont) == num1:
            print(min(cont) + max(cont))