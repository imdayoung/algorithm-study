import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1] * N 
num = [[A[i]] for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                num[i] = num[j] + [A[i]]
                dp[i] = dp[j] + 1

max_value = max(dp)
for i in range(N):
    if dp[i] == max_value:
        print(dp[i])
        print(*num[i])
        exit()