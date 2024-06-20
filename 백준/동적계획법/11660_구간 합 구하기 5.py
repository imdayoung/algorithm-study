# import sys
# input = sys.stdin.readline

# table = []
# n, m = map(int, input().split())
# for _ in range(n):
#     table.append(list(map(int, input().split())))

# for _ in range(m):
#     answer = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1 - 1, x2):
#         for j in range(y1 - 1, y2):
#             answer += table[i][j]
#     print(answer)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0] * (n + 1) for _ in range((n + 1))]
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + table[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)