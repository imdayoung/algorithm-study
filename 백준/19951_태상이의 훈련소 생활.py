import sys


N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for a, b, k in orders:
    for i in range(a - 1, b):
        H[i] += k

print(*H)
