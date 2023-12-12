from solver import parse, arrangements
from collections import Counter

with open("test_input.txt", "r") as f:
    lines = f.read().split("\n")[:-1]
lengths = []
for line in lines:
    sequence = parse(line)
    l = arrangements(sequence)
    if l is not None:
        lengths.append(l)

print(len(lengths))
print(Counter(lengths))
    
#     # new_len, _ = sequence
#     new_len = arrangements(sequence)
#     lengths.append(new_len)

# print(Counter(lengths))
#     if len(new_len) > max:
#         max = len(new_len)
# print(max)

