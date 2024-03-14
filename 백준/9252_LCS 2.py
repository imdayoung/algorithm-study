import sys


string1 = ' ' + sys.stdin.readline().rstrip()
string2 = ' ' + sys.stdin.readline().rstrip()
n, m = len(string1), len(string2)

dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

answer_len = dp[-1][-1]
answer_str = ''

i, j = n - 1, m - 1
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        answer_str += string1[i]
        i -= 1
        j -= 1

print(answer_len)
if answer_len > 0:
    print(answer_str[::-1])