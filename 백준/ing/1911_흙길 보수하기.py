import sys


answer = 0

N, L = map(int, sys.stdin.readline().split())
road = [0 for _ in range(1000000000 + 1)]

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())


# # 메모리 초과
# import sys


# answer = 0

# N, L = map(int, sys.stdin.readline().split())
# road = [0 for _ in range(1000000000 + 1)]
# min_idx, max_idx = 1000000000, 0

# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     for i in range(start, end):
#         road[i] = 1

#     min_idx = min(min_idx, start)
#     max_idx = max(max_idx, end)

# for i in range(min_idx, max_idx):
#     if road[i] == 1:
#         answer += 1
#         for j in range(i, i + L):
#             road[j] = 0

# print(answer)