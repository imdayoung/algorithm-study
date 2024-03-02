import sys


N = int(sys.stdin.readline())
counselors = []
for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    counselors.append((T, P))

dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    if i + counselors[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + counselors[i][0]] + counselors[i][1])

print(dp[0])