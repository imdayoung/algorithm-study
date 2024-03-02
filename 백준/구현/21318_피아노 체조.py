import sys
input = sys.stdin.readline

N = int(input())
levels = list(map(int, input().split()))

mistake = [0] * N
for i in range(1, N):
    if levels[i - 1] > levels[i]:
        mistake[i] = mistake[i - 1] + 1
    else:
        mistake[i] = mistake[i - 1]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(mistake[y - 1] - mistake[x - 1])

# 범위 상 오류가 있음
# import sys
# input = sys.stdin.readline

# N = int(input())
# levels = list(map(int, input().split()))

# mistake = [0] * N
# for i in range(1, N - 1):
#     if levels[i] > levels[i + 1]:
#         mistake[i] = mistake[i - 1] + 1
#     else:
#         mistake[i] = mistake[i - 1]
# mistake[-1] = mistake[-2]
# print(mistake)

# Q = int(input())
# for _ in range(Q):
#     x, y = map(int, input().split())
#     if x == y:
#         answer = 0
#     else:
#         if x >= 2 and y >= 2:
#             answer = mistake[y - 2] - mistake[x - 2]
#         elif x < 2:
#             answer = mistake[y - 2]
#     print(answer)

# 시간 초과
# import sys
# input = sys.stdin.readline

# answer = []

# N = int(input())
# levels = list(map(int, input().split()))
# Q = int(input())
# for _ in range(Q):
#     cnt = 0
#     x, y = map(int, input().split())
#     play = levels[x - 1:y]
#     for i in range(y - x):
#         if play[i] > play[i + 1]:
#             cnt += 1
#     answer.append(cnt)

# for a in answer:
#     print(a)