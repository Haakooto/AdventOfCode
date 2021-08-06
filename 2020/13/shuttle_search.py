import numpy as np

lines = open("test").read().splitlines()
time = int(lines[0])
all_shuttles = np.array([(j, i) for j, i in enumerate(lines[1].split(","))])
all_shuttles = np.array(
    [(int(j) % int(i), int(i)) for j, i in all_shuttles if i != "x"]
)
a, shuttles = all_shuttles.T
time_to_next = shuttles - time % shuttles
first = np.argmin(time_to_next)
print(shuttles[first] * time_to_next[first])


all = np.asarray(sorted(all_shuttles, key=lambda x: x[1])[::-1])
# a = np.arange(len(all_shuttles))
# a = np.array([i for i in np.arange(len(all_shuttles)) if all_shuttles[i] != "x"])
# n = shuttles
print(all)
# print(a)
# print(shuttles)

x = all[0, 0]
for i in range(len(all) - 1):
    # x = a
    # k = 0
    while x % all[i + 1, 1] != all[i + 1, 0]:
        x += np.prod(all[: i + 1, 1])
        # k += 1
    # print(k)
    # print(x)
    # sys
print(x)
x = 1068781
for a, n in all:
    print(a, n, x % n)
while True:
    print(x := x / 2)
    input()
# n = [3, 4, 5]
# a = [0, 3, 4]

# for i in range(len(n)-1):
#     for j in (range(100)):
#         xi = a[i] + j * np.prod(n[: i + 1])
#         if xi == a[i + 1]:
#             break
#     if not xi:
#         break
# print(xi)
