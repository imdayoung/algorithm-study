import sys
input = sys.stdin.readline

N = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))

# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# dp_max = [[0] * 3 for _ in range(2)]
# dp_min = [[0] * 3 for _ in range(2)]

# for i in range(3):
#     dp_max[0][i] = board[0][i]
#     dp_min[0][i] = board[0][i]

# for i in range(1, N):
#     dp_max[1][0] = board[i][0] + max(dp_max[0][0], dp_max[0][1])
#     dp_max[1][1] = board[i][1] + max(dp_max[0][0], dp_max[0][1], dp_max[0][2])
#     dp_max[1][2] = board[i][2] + max(dp_max[0][1], dp_max[0][2])

#     dp_min[1][0] = board[i][0] + min(dp_min[0][0], dp_min[0][1])
#     dp_min[1][1] = board[i][1] + min(dp_min[0][0], dp_min[0][1], dp_min[0][2])
#     dp_min[1][2] = board[i][2] + min(dp_min[0][1], dp_min[0][2])

#     dp_max[0] = dp_max[1]
#     dp_min[0] = dp_min[1]
#     dp_max[1] = [0, 0, 0]
#     dp_min[1] = [0, 0, 0]
    
# print(max(dp_max[0]), min(dp_min[0]))