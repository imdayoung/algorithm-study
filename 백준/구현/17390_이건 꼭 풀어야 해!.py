import sys


answers = []

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

dp = [0 for _ in range(N + 1)]
dp[1] = A[0]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + A[i - 1]

for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    answers.append(dp[R] - dp[L - 1])

for answer in answers:
    print(answer)
