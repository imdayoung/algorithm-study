from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for k in range(1,  N + 1):
    combs = list(combinations(nums, k))
    print(combs)
    for comb in combs:
        if sum(comb) == S:
            count += 1

print(count)