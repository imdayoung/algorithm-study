# DFS
import sys
sys.setrecursionlimit(10 ** 6)


def travel(start):
    global answer

    visited[start] = True
    cur_visited.append(start)

    next_student = students[start]
    # 방문하지 않았던 학생을 방문하게 되는 경우 계속 탐색 진행
    if not visited[next_student]:
        travel(next_student)
    else:
        # 사이클이 생기면 사이클의 길이만큼 팀이 생성됨
        if next_student in cur_visited:
            answer -= len(cur_visited[cur_visited.index(next_student):])
        return


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    students = [0] + list(map(int, sys.stdin.readline().split()))

    answer = n
    visited = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        if not visited[i]:
            # 현재 탐색하는 중 방문하게 되는 학생들의 리스트
            cur_visited = []
            travel(i)

    print(answer)


# # BFS
# import sys
# from collections import deque


# def travel(start):
#     queue = deque([start])
#     visited[start] = True
#     cur_visited = [start]

#     while queue:
#         std = queue.popleft()
#         next_std = students[std]
#         if visited[next_std]:
#             if next_std in cur_visited:
#                 return len(cur_visited[cur_visited.index(next_std):])
#             else:
#                 return 0
#         else:
#             visited[next_std] = True
#             queue.append(next_std)
#             cur_visited.append(next_std)

#     return 0


# T = int(sys.stdin.readline())
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     students = [0] + list(map(int, sys.stdin.readline().split()))
    
#     answer = n
#     visited = [False for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         if not visited[i]:
#             answer -= travel(i)

#     print(answer)