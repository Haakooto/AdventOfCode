# from main import alt

# if alt == 1:
#     from solver import solver_alt1 as solver
# elif alt == 2:
#     from solver import solver_alt2 as solver
# elif alt == 3:
#     from solver import solver1_alt3 as solver1, solver2_alt3 as solver2
# from solver import func_that_does_the_thing
# from solver import Part

# test1 = "test_input.txt"
# solver2(test1)

from itertools import product
from time import time
from collections import Counter
ranges = {
    'A': (1, 100),
    'B': (20, 200),
    # ... add more ranges here
}

ranges = {
    'x': (1416, 4000), 
    'm': (1, 4000), 
    'a': (2006, 4000), 
    's': (1351, 4000),
}
ranges = {
    'x': (1, 4000), 
    'm': (1, 4000), 
    'a': (1, 4000), 
    's': (1, 4000),
}

ranges =  {
    'x': (1, 1415),
     'm': (1, 4000),
     'a': (1, 2005),
     's': (1, 1350),
}

# ranges = {
#     'A': (1, 3),
#     'B': (2, 4),
#     'C': (0, 2),
#     'D': (5, 7)
# }

# ranges = {
#     'A': (1, 3),
#     'B': (2, 3),
#     'C': (0, 2),
#     'D': (5, 8),
# }

print(ranges)

base = sum([low for low, high in ranges.values()])
incl_range = lambda a, b: range(a, b + 1)  # inclusive range
all_combinations = product(*[incl_range(*rang) for rang in ranges.values()])  # all combinations
sums_of_4_numbers = [sum(combination) for combination in all_combinations]  # sums of 4 numbers
coeffs = Counter(sums_of_4_numbers)  # number of times each sum appears
sum_of_ranges = sum([coeff * sum for sum, coeff in coeffs.items()])  # sum of all sums
print(sum_of_ranges)


from functools import reduce
from operator import mul

def number_of_combinations(range_tuple):
    a, b = range_tuple
    return b - a + 1

total_combinations = reduce(mul, (number_of_combinations(value) for value in ranges.values()))
average_sum = sum((b + a) / 2.0 for a, b in ranges.values())
result = int(total_combinations * average_sum)

print(167409079868000)
print(result)
