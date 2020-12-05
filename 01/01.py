import numpy as np

with open("data.txt", "r") as f:
    d = np.array([int(i.strip()) for i in f.read().split()[:-1]])
a, b, c = np.meshgrid(d, d, d)

print(np.prod(d[np.where((a + b)[:, :, 0] == 2020)[0]]))
print(np.prod(d[np.array(np.where(a + b + c == 2020))[:, 0]]))
