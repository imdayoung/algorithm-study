# 누적 합
import sys


N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

orders = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b, k = map(int, sys.stdin.readline().split())
    orders[a - 1] += k
    orders[b] -= k
    
for i in range(N):
    orders[i + 1] += orders[i]
    H[i] += orders[i]
    
print(*H)
