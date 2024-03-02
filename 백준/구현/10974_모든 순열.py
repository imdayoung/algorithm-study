from itertools import permutations

n = int(input())
nums = [i for i in range(1, n + 1)]

lst = list(permutations(nums, n))

for l in lst:
    print(*l)