import sys


N = int(sys.stdin.readline())

if N == 1:
    print(0)
    exit()

dp = [0 for _ in range(N + 1)]
dp[2] = 1

for i in range(3, N + 1):
    if i % 2 == 0:
        dp[i] = (dp[i - 1] * 2 + 1) % 1000000007
    else:
        dp[i] = (dp[i - 1] * 2 - 1) % 1000000007

print(dp[-1])


# # 음 이건 분명히 아닌 것 같다
# import sys
# sys.setrecursionlimit(10 ** 6)

# def backtracking(num, len_cnt):
#     global answer
    
#     if len_cnt == N:
#         if int(num) % 15 == 0:
#             answer += 1
#         return
    
#     backtracking(num + "1", len_cnt + 1)
#     backtracking(num + "5", len_cnt + 1)
    

# answer = 0

# N = int(sys.stdin.readline())
# backtracking("", 0)
# print(answer)
