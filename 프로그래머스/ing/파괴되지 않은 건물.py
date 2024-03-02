def solution(board, skill):
    answer = 0
    return answer

# # 시간초과 ..
# def solution(board, skill):
#     n, m = len(board), len(board[0])
#     answer = n * m

#     for s in skill:
#         skill_type = s[0]
#         r1, c1, r2, c2 = s[1], s[2], s[3], s[4]
#         degree = s[5]

#         if skill_type == 1:
#             for i in range(r1, r2 + 1):
#                 for j in range(c1, c2 + 1):
#                     if board[i][j] > 0 and board[i][j] - degree <= 0:
#                         answer -= 1
#                     board[i][j] -= degree
#         else:
#             for i in range(r1, r2 + 1):
#                 for j in range(c1, c2 + 1):
#                     if board[i][j] <= 0 and board[i][j] + degree > 0:
#                         answer += 1
#                     board[i][j] += degree

#     return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
# 10
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
# 6