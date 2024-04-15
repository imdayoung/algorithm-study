import sys


string1 = ' ' + sys.stdin.readline().rstrip()
string2 = ' ' + sys.stdin.readline().rstrip()
n = len(string1)
m = len(string2)

dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])