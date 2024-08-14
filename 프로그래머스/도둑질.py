def solution(money):
    answer = 0
    n = len(money)
    
    if n == 3:
        return max(money[0], money[1], money[2])
    
    # 첫째 집을 터는 경우 / 둘째 집을 터는 경우 / 둘 다 털지 않는 경우
    dp1 = [[0 for _ in range(2)] for _ in range(n)]
    dp2 = [[0 for _ in range(2)] for _ in range(n)]
    dp3 = [[0 for _ in range(2)] for _ in range(n)]
    
    # dp1, 첫째 집을 터는 경우
    dp1[0][1] = money[0]
    dp1[1][0] = money[0]
    
    for i in range(2, n):
        dp1[i][0] = max(dp1[i - 1][0], dp1[i - 1][1])
        dp1[i][1] = dp1[i - 1][0] + money[i]
    
    # dp2, 둘째 집을 터는 경우
    dp2[1][1] = money[1]
    dp2[2][0] = money[1]
    
    for i in range(3, n):
        dp2[i][0] = max(dp2[i - 1][0], dp2[i - 1][1])
        dp2[i][1] = dp2[i - 1][0] + money[i]
    
    # dp3, 둘 다 털지 않는 경우
    dp3[2][1] = money[2]
    dp3[3][0] = money[2]
    
    for i in range(4, n):
        dp3[i][0] = max(dp3[i - 1][0], dp3[i - 1][1])
        dp3[i][1] = dp3[i - 1][0] + money[i]
        
    answer = max(dp1[n - 1][0], dp2[n - 1][0], dp2[n - 1][1], dp3[n - 1][0], dp3[n - 1][1])
    
    return answer


# # 시간 초과
# def solution(money):
#     answer = 0
#     n = len(money)
    
#     if n == 3:
#         return max(money[0], money[1], money[2])
    
#     # 첫째 집을 터는 경우 / 둘째 집을 터는 경우 / 둘 다 털지 않는 경우
#     dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(3)]
#     dp[0][0][1] = money[0]
#     dp[0][1][0] = money[0]
#     dp[1][1][1] = money[1]
#     dp[1][2][0] = money[1]
#     dp[2][2][1] = money[2]
#     dp[2][3][0] = money[2]
    
#     for i in range(2, n):
#         dp[0][i][0] = max(dp[0][i - 1][0], dp[0][i - 1][1])
#         dp[0][i][1] = dp[0][i - 1][0] + money[i]
        
#         if i == 2:
#             continue

#         dp[1][i][0] = max(dp[1][i - 1][0], dp[1][i - 1][1])
#         dp[1][i][1] = dp[1][i - 1][0] + money[i]

#         if i == 3:
#             continue

#         dp[2][i][0] = max(dp[2][i - 1][0], dp[2][i - 1][1])
#         dp[2][i][1] = dp[2][i - 1][0] + money[i]
        
#     answer = max(dp[0][-1][0], dp[1][-1][0], dp[1][-1][1], dp[2][-1][0], dp[2][-1][1])
#     return answer
