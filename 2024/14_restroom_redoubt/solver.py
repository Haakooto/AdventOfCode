import re
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import defaultdict


def read(file):
    with open(file, "r") as file:
        lines = file.read().split("\n") # Most typical case
    *robots, size = lines
    robots = [re.findall(r'-?\d+', robot) for robot in robots]
    for r in range(len(robots)):
        robots[r] = [int(i) for i in robots[r]]
    return robots, size.split(",")

def extended_gcd(a, b):
    """
    Compute the greatest common divisor of a and b using the Extended Euclidean Algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def first_coincidence(period_a, first_a, period_b, first_b):
    """
    Find the first time t ≥ 0 when two periodic events coincide.
    
    Event A occurs at t = first_a + n*period_a for n ≥ 0.
    Event B occurs at t = first_b + m*period_b for m ≥ 0.
    
    We want to solve:
        first_a + period_a*k = first_b + period_b*j

    This can be handled by solving the linear congruence:
        period_a * k ≡ (first_b - first_a) (mod period_b).

    If no non-negative solution exists, the function returns None.
    """
    # Shift
    diff = first_b - first_a
    pa = period_a
    pb = period_b

    # Solve pa*k ≡ diff (mod pb)
    # This is solvable if gcd(pa, pb) divides diff.
    g, x, y = extended_gcd(pa, pb)
    if diff % g != 0:
        # No solution exists
        return None

    # Simplify the equation by dividing through the gcd
    pa_ = pa // g
    pb_ = pb // g
    diff_ = diff // g

    # A particular solution for pa_*x ≡ diff_ (mod pb_) is given by x * diff_
    # where x is the inverse of pa_ mod pb_. From extended_gcd, we know:
    # pa_*x + pb_*y = 1, so x is the modular inverse of pa_ modulo pb_.
    k = (x * diff_) % pb_

    # The first coinciding time
    t = first_a + pa*k

    return t

# print(first_coincidence(101, 62, 103, 25))  # Should print 7132

def solver_alt2(input_file):
    robots, (X, Y) = read(input_file)
    X, Y = int(X), int(Y)
    times = 3000
    hist = np.zeros((times, Y, X))
    stats = defaultdict(list)
    for time in tqdm(range(times), desc="Simulating..."):
        room = np.zeros((Y, X))
        xs = np.zeros(len(robots))
        ys = np.zeros(len(robots))
        for i, r in enumerate(robots):
            x = (r[0] + r[2] * time) % X
            y = (r[1] + r[3] * time) % Y
            xs[i] = x
            ys[i] = y
            room[y, x] += 1
        hist[time] = room

        stats["x_mean"].append(np.mean(xs))
        stats["y_mean"].append(np.mean(ys))
        stats["x_std"].append(np.std(xs))
        stats["y_std"].append(np.std(ys))
        stats["room_mean"].append(np.mean(room))
        stats["room_std"].append(np.std(room))
        stats["room_max"].append(np.max(room))

        # Threshold determined by visual inspection of plots
        if np.std(xs) < 25:
            stats["xlow"].append(time)
        if np.std(ys) < 25:
            stats["ylow"].append(time)

        if time == 100:
            q1 = np.sum(room[:Y//2, :X//2])
            q2 = np.sum(room[Y//2+1:, :X//2])
            q3 = np.sum(room[:Y//2, X//2+1:])
            q4 = np.sum(room[Y//2+1:, X//2+1:])
            part1 = q1 * q2 * q3 * q4

    """
    Looking at std-plots, I see a constant, periodic outlier, 
    where all robots are much closer in either x or y direction.
    I (correctly) postulated the time of first tree will be when this lumping 
    happens in both x and y direction. Need to find that time. 
    Shamelessly steal function for solving this problem, given periods and first occurances :)
    """
    diffs_x = [i - j for i, j in zip(stats["xlow"][1:], stats["xlow"][:-1])]
    diffs_y = [i - j for i, j in zip(stats["ylow"][1:], stats["ylow"][:-1])]
    diff_x = diffs_x[0]
    diff_y = diffs_y[0]
    first_x = stats["xlow"][0]
    first_y = stats["ylow"][0]
    part2 = first_coincidence(diff_x, first_x, diff_y, first_y)

    # Plot stats to determine threshold
    for stat, vals in stats.items():
        plt.plot(vals, "bo")
        plt.title("stat")
        plt.savefig(f"{stat}.png")
        plt.clf()

    tree = np.zeros((Y, X))
    for i, r in enumerate(robots):
        x = (r[0] + r[2] * part2) % X
        y = (r[1] + r[3] * part2) % Y
        tree[y, x] += 1
    plt.imshow(tree)
    plt.title(f"Time = {part2}")
    plt.savefig("tree.png")

    return part1, part2
    
