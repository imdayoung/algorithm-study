import sys
input = sys.stdin.readline


N = int(input())
card = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = card[i]

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i - j] + card[j])

print(dp[N])