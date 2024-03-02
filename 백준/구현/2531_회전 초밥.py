import sys
input = sys.stdin.readline

answer = 0
N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]
# 리스트를 두 개를 이어붙임
sushis.extend(sushis)

for i in range(N + 1):
    continuous = set(sushis[i:i + k])
    if c not in continuous:
        temp = len(continuous) + 1
    else:
        temp = len(continuous)
    if temp > answer:
        answer = temp

print(answer)