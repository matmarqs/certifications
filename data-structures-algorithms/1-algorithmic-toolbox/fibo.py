#!/usr/bin/env python3

def f(n):
    if n <= 1:
        return n
    f0 = 0
    f1 = 1
    for i in range(2, n+1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2

def main():
    print(f(int(input())))

if __name__ == '__main__':
    main()
