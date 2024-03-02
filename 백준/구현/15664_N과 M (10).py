from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
comb = sorted(list(set(list(combinations(nums, m)))))

for c in comb:
    print(*c)