import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time


def follow_rule(N):
    N = np.asarray([int(n) for n in str(N)])
    M = np.asarray([N[i + 1] - N[i] for i in range(5)])

    if not (M >= 0).all():
        return False

    if not (M == 0).any():
        return False

    group = False
    double = False
    for i in range(1, 10):
        r = np.count_nonzero(N == i)
        if r == 2:
            double = True
        elif r > 2:
            group = True
    if double:
        return True
    else:
        return not group
    # A = np.argwhere(M == 0)
    # if not A.shape[0]:
    #     if A.shape[0] == 1:
    #         return True
    #     elif 
    # else:
    #     return True



def main():
    count = 0
    for N in range(152085, 670283):
        if follow_rule(N):
            count += 1

    print(count)

if __name__ == "__main__":
    main()
