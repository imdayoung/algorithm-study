# 1, 2, 3 중 한 개만 홀수개일 수 있음
import sys


T = int(sys.stdin.readline())

dp = [0 for _ in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 2

for i in range(4, 100001):
    dp[i]
    
for _ in range(T):
    n = int(sys.stdin.readline())
    