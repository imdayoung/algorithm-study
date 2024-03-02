import sys


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

A, B = map(int, sys.stdin.readline().split())
print("1" * gcd(A, B))