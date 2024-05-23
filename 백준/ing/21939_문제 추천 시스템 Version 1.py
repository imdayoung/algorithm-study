import sys
import heapq


problems = {}
problems_rev = {}
problems_num = {}

N = int(sys.stdin.readline())

# 문제 리스트에 추가할 문제 번호와 난이도 입력
for _ in range(N):
    P, L = map(int, sys.stdin.readline().split())
    if L not in problems:
        problems[L] = [P]
        problems_rev[L] = [-P]
        problems_num[P] = [L]
    else:
        heapq.heappush(problems[L], P)
        heapq.heappush(problems_rev[L], -P)
        heapq.heappush(problems_num[P], L)

M = int(sys.stdin.readline())
for i in range(M):
    print(i + 1)
    print(problems)
    print(problems_rev)
    print(problems_num)
    command = list(map(str, sys.stdin.readline().rstrip().split()))

    # 가장 어렵거나 가장 쉬운 문제 번호 출력
    if command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            hardest = max(problems.keys())
            temp = heapq.heappop(problems_rev[hardest])
            print(-temp)
            heapq.heappush(problems_rev[hardest], temp)
        elif x == -1:
            easiest = min(problems.keys())
            temp = heapq.heappop(problems[easiest])
            print(temp)
            heapq.heappush(problems[easiest], temp)
            
    # 추천 문제 리스트에 난이도가 L인 문제 번호 P 추가
    elif command[0] == 'add':
        P = int(command[1])
        L = int(command[2])
        if L not in problems:
            problems[L] = [P]
            problems_rev[L] = [-P]
            problems_num[P] = [L]
        else:
            heapq.heappush(problems[L], P)
            heapq.heappush(problems_rev[L], -P)
            heapq.heappush(problems_num[P], L)
        
    # 추천 문제 리스트에서 문제 번호 P 제거
    elif command[0] == 'solved':
        P = int(command[1])
        while problems_num[P]:
            level = heapq.heappop(problems_num[P])
            problems[level].remove(P)
            problems_rev[level].remove(-P)
            if problems[level] == []:
                del problems[level]
            if problems_rev[level] == []:
                del problems_rev[level]
        del problems_num[P]


# # 19M 58S -> 시간 초과
# import sys


# problems = {i:[] for i in range(1, 100 + 1)}
# problems_rev = {}

# N = int(sys.stdin.readline())

# for _ in range(N):
#     P, L = map(int, sys.stdin.readline().split())
#     problems[L].append(P)
#     if P not in problems_rev:
#         problems_rev[P] = [L]
#     else:
#         problems_rev[P].append(L)

# M = int(sys.stdin.readline())
# for _ in range(M):
#     command = list(map(str, sys.stdin.readline().rstrip().split()))

#     if command[0] == 'recommend':
#         x = command[1]
#         if x == '1':
#             for i in range(100, 0, -1):
#                 if problems[i] != []:
#                     print(max(problems[i]))
#                     break
#         elif x == '-1':
#             for i in range(1, 100 + 1):
#                 if problems[i] != []:
#                     print(min(problems[i]))
#                     break

#     elif command[0] == 'add':
#         P = int(command[1])
#         L = int(command[2])
#         problems[L].append(P)
#         if P not in problems_rev:
#             problems_rev[P] = [L]
#         else:
#             problems_rev[P].append(L)

#     elif command[0] == 'solved':
#         P = int(command[1])
#         for level in problems_rev[P]:
#             problems[level].remove(P)
#         problems_rev.pop(P)
