N = int(input())
dp = [0] * (N + 1)

if N < 3:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[N])


# # 시간 초과
# import sys
# sys.setrecursionlimit(10 ** 6)


# def is_pinary(n):
#     if n[0] == 0:
#         return False
#     for i in range(len(n) - 1):
#         if n[i] == 1 and n[i] == n[i + 1]:
#             return False
#     return True
  

# def backtracking():
#     global arr
#     global answer
  
#     if len(arr) == N:
#         if is_pinary(arr):
#             answer += 1
#         return

#     for i in range(2):
#         arr.append(i)
#         backtracking()
#         arr.pop()
  

# answer = 0
# N = int(input())
# arr = [1]
# backtracking()
# print(answer)