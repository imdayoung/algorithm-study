import sys
input = sys.stdin.readline


n = int(input())

lines = [tuple((map(int, input().split()))) for _ in range(n)]
lines = sorted(lines, key = lambda x : x[0])

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))