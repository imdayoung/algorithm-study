import sys


N, K, B = map(int, sys.stdin.readline().split())

answer = N
lights = [1 for _ in range(N + 1)]

for _ in range(B):
    broken = int(sys.stdin.readline())
    lights[broken] = 0

start, end = 1, K
fix = lights[start:end + 1].count(0)

while end < N:
    start += 1
    end += 1
    if lights[end] == 0:
        fix += 1
    if lights[start - 1] == 0:
        fix -= 1
    answer = min(answer, fix)
    
print(answer)
