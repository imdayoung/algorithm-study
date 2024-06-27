import sys


N = int(sys.stdin.readline())


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
