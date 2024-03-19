

# # 시간 초과
# n = int(input())

# a = 0
# b = 1
# answer = 0
# for _ in range(n - 1):
#     answer = (a + b) % 1000000007
#     a = b
#     b = answer

# print(answer)

# # 메모리 초과
# n = int(input())

# dp = [0] * (n + 2)
# dp[2] = 1
# for i in range(3, n + 2):
#     dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

# print(dp[n + 1])