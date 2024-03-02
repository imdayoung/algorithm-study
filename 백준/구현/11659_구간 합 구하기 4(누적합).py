import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
sums = [0 for _ in range(n)]
sums[0] = nums[0]
for i in range(n):
    sums[i] = sums[i - 1] + nums[i]

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    if x == 1:
        print(sums[y - 1])
    else:
        print(sums[y - 1] - sums[x - 2])