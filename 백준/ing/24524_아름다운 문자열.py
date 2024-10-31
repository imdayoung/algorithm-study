# # 시간 초과
# import sys


# answer = 0
# S = sys.stdin.readline().rstrip()
# T = sys.stdin.readline().rstrip()
# n = len(S)
# m = len(T)

# visited = [False for _ in range(n)]
# while True:
#     cur_index = 0
#     for i in range(n):
#         if not visited[i] and S[i] == T[cur_index]:
#             visited[i] = True
#             cur_index += 1
#         if cur_index == m:
#             answer += 1
#             break
#     else:
#         break
        
# print(answer)
