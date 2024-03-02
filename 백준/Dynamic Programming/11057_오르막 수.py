import sys

N = int(sys.stdin.readline())
dp = [[1] * 10 for _ in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, 10):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(sum(dp[N]) % 10007)

# import sys
# sys.setrecursionlimit(10 ** 6)

# def back_tracking(start):
#     global answer
#     if len(arr) == N:
#         answer = (answer + 1)
#         return
    
#     for i in range(start, 10):
#         arr.append(i)
#         back_tracking(i)
#         arr.pop()


# answer = 0
# N = int(sys.stdin.readline())
# arr = []
# back_tracking(0)
# print(answer)