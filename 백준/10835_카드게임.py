import sys


N = int(sys.stdin.readline())
left = list(map(int, sys.stdin.readline().split()))
right = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        if right[j] < left[i]:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1] + right[j])
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])
    

# import sys
# from collections import deque


# answer = 0

# N = int(sys.stdin.readline())
# left = deque(list(map(int, sys.stdin.readline().split())))
# right = deque(list(map(int, sys.stdin.readline().split())))
# max_left = max(left)

# while left and right:
#     if right[0] < left[0]:
#         answer += right.popleft()
#     elif right[0] >= max_left:
#         left.popleft()
#         right.popleft()
#     else:
#         temp = left.popleft()
#         if temp == max_left:
#             max_left = max(left)

# print(answer)