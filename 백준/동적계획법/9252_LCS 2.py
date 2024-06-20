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


# # 시간 초과
# import sys


# string1 = ' ' + sys.stdin.readline().rstrip()
# string2 = ' ' + sys.stdin.readline().rstrip()
# n, m = len(string1), len(string2)

# dp_str = [['' for _ in range(m)] for _ in range(n)]

# for i in range(1, n):
#     for j in range(1, m):        
#         if string1[i] == string2[j]:
#             dp_str[i][j] = dp_str[i - 1][j - 1] + string1[i]

#         else:
#             if len(dp_str[i - 1][j]) > len(dp_str[i][j - 1]):
#                 dp_str[i][j] = dp_str[i - 1][j]

#             else:
#                 dp_str[i][j] = dp_str[i][j - 1]


# print(len(dp_str[-1][-1]))
# if len(dp_str[-1][-1]) > 0:
#     print(dp_str[-1][-1])


# # 시간 초과
# string1 = ' ' + input()
# string2 = ' ' + input()
# n = len(string1)
# m = len(string2)

# dp_str = [['' for _ in range(m)] for _ in range(n)]
# dp_len = [[0 for _ in range(m)] for _ in range(n)]

# for i in range(1, n):
#     for j in range(1, m):        
#         if string1[i] == string2[j]:
#             dp_len[i][j] = dp_len[i - 1][j - 1] + 1
#             dp_str[i][j] = dp_str[i - 1][j - 1] + string2[j]

#         else:
#             if dp_len[i - 1][j] > dp_len[i][j - 1]:
#                 dp_len[i][j] = dp_len[i - 1][j]
#                 dp_str[i][j] = dp_str[i - 1][j]

#             else:
#                 dp_len[i][j] = dp_len[i][j - 1]
#                 dp_str[i][j] = dp_str[i][j - 1]

# answer_len = dp_len[n - 1][m - 1]
# print(answer_len)
# if answer_len > 0:
#     print(dp_str[n - 1][m - 1])