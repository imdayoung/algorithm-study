import sys


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(21)] for _ in range(N)]
dp[0][nums[0]] = 1

for idx in range(1, N - 1):
    for target_number in range(21):
        if target_number - nums[idx] >= 0:
            dp[idx][target_number] = dp[idx - 1][target_number - nums[idx]]
        if target_number + nums[idx] <= 20:
            dp[idx][target_number] += dp[idx - 1][target_number + nums[idx]]

print(dp[N - 2][nums[-1]])


# # 메모리 초과
# import sys
# from collections import deque


# def bfs(start, idx):
#     answer = 0
#     queue = deque([(start, idx)])
#     while queue:
#         num, idx = queue.popleft()
#         if idx == N - 2:
#             if num == nums[-1]:
#                 answer += 1
#             continue

#         for next_num in [num + nums[idx + 1], num - nums[idx + 1]]:
#             if next_num > 20 or next_num < 0:
#                 continue
#             queue.append((next_num, idx + 1))
        
#     return answer

# N = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
# print(bfs(nums[0], 0))