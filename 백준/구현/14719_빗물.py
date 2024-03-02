import sys


answer = 0
H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

for i in range(1, W - 1):
    left = block[:i]
    right = block[i + 1:]

    compare = min(max(left), max(right))
    if block[i] < compare:
        answer += compare - block[i]

print(answer)