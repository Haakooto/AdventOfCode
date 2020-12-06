import numpy as np

char, passw = np.loadtxt("data.txt", dtype=str, converters={1: lambda s: s[:-1]}, usecols=(1,2), unpack=True)
num = np.loadtxt("data.txt", dtype=int, converters={0: lambda s: s.split(b"-")}, usecols=(0), ndmin=2)


def val1(mn, mx, l, wrd):
    cnt = wrd.count(l)
    return mn <= cnt <= mx


def val2(mn, mx, l, wrd):
    a = wrd[mn - 1] == l
    b = wrd[mx - 1] == l
    return (a+b) == 1


for val in (val1, val2):
    s = 0
    for ns, letter, pasw in zip(num, char, passw):
        if val(*ns, letter, pasw):
            s += 1
    print(s)
