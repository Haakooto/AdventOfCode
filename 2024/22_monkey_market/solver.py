from numpy import zeros
from collections import defaultdict

def read(file):
    with open(file, "r") as file:
        return file.read().split("\n")[:-1]

def rng(num):
    num ^= (num * 64)
    num %= 16777216
    num ^= (int(num / 32))
    num %= 16777216
    num ^= (num * 2048)
    num %= 16777216
    yield num

def gen_seq(inpt, iters):
    sec = int(inpt)
    vals = zeros(iters+1, dtype=int)
    for i in range(iters):
        vals[i] = int(str(sec)[-1])
        sec = next(rng(sec))
    vals[-1] = int(str(sec)[-1])
    return sec, vals

def solver_alt2(input_file):
    lines = read(input_file)
    sum = 0

    prices = []
    changes = []
    for num in lines:
        last, price = gen_seq(num, 2000)
        sum += last
        prices.append(price)
        changes.append(price[1:] - price[:-1])

    bananas = defaultdict(int)
    for price, change in zip(prices, changes):
        cust = set()
        for i in range(len(change) - 3):
            p = price[i+4]
            cs = tuple(change[i:i+4])
            if cs not in cust:
                bananas[cs] += p
            cust.add(cs)

    return sum, max(bananas.values())
