#!/usr/bin/env python3

import random
import sys

# n = len(L), complexity O(n)
def max2prod(n, L):
    max1, max2 = 0, 0
    for i in range(n):
        if L[i] > max1:
            max2 = max1
            max1 = L[i]
        elif L[i] > max2:
            max2 = L[i]
    return max1 * max2


# complexity O(n^2)
def max2prod_slow(n, L):
    maxprod = 0
    for i in range(n):
        for j in range(i+1, n):
            prod = L[i] * L[j]
            if prod > maxprod:
                maxprod = prod
    return maxprod


# check if the two algorithms differ
def stress_test():
    if len(sys.argv) > 1:
        random.seed(int(sys.argv[1]))
    else:
        random.seed(1)
    while True:
        #n = random.randint(2, 200000)
        #L = [random.randint(2, 100000) for i in range(n)]
        n = random.randint(2, 10)
        L = [random.randint(2, 100) for i in range(n)]
        print(n)
        print(L)
        res1 = max2prod(n, L)
        res2 = max2prod_slow(n, L)
        if res1 != res2:
            print(f"Wrong: {res1} {res2}")
            break   # the algorithms differ, quit.
        else:
            print("OK")


def main():
    n = int(input())
    L = list(map(int, input().split()))
    print(max2prod(n, L))


if __name__ == '__main__':
    stress_test()
    #main()
