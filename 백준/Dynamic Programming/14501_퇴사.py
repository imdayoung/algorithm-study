import sys
input = sys.stdin.readline

n = int(input().rstrip())

schedule = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않음
    if i + schedule[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        # i일에 상담을 하는 것과 상담을 안 하는 것 중 큰 것 선택
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[i + schedule[i][0]])
        
print(dp[0])