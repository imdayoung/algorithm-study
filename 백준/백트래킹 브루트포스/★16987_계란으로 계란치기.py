# https://kjhoon0330.tistory.com/entry/BOJ-16987-%EA%B3%84%EB%9E%80%EC%9C%BC%EB%A1%9C-%EA%B3%84%EB%9E%80%EC%B9%98%EA%B8%B0-Python

import sys
# sys.stdin = open("input_16987.txt", "r")
input = sys.stdin.readline


def attack(left):
    global answer
    
    # 종료 조건
    if left == N:
        breaked = 0
        for i in range(N):
            if eggs[i][S] <= 0:
                breaked += 1
        answer = max(answer, breaked)
        return

    # 왼손에 든 계란이 깨진 계란인 경우 다음 계란으로
    if eggs[left][S] <= 0:
        attack(left + 1)
        return
    
    # 모든 계란이 깨져있는 경우
    for i in range(N):
        if i == left:
            continue
        if eggs[i][S] > 0:
            break
    else:
        answer = max(answer, N - 1)
        return

    # 공격!
    for i in range(N):
        if i == left or eggs[i][S] <= 0:
            continue
        eggs[i][S] -= eggs[left][W]
        eggs[left][S] -= eggs[i][W]
        attack(left + 1)
        # 복구
        eggs[i][S] += eggs[left][W]
        eggs[left][S] += eggs[i][W]


answer = 0
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
S, W = 0, 1
attack(0)
print(answer)

# import sys
# sys.stdin = open("input_16987.txt", "r")
# input = sys.stdin.readline

# def attack(left):
#     s = eggs[left][1] # 왼쪽 손에 들고 있는 계란의 내구도
#     w = eggs[left][2] # 왼쪽 손에 들고 있는 계란의 무게

#     for i in range(N):
#         if eggs_sort[i][0] == left:
#             left_in_sorted = i
#             break

#     for i in range(N):
#         if eggs_sort[i][0] == left or eggs_sort[i][1] == 0:
#             continue

#         eggs_sort[i][1] -= w
#         eggs_sort[left_in_sorted][1] -= eggs_sort[i][2]
#         if eggs_sort[i][1] < 0:
#             eggs_sort[i][1] = 0
#         if eggs_sort[left_in_sorted][1] < 0:
#             eggs_sort[left_in_sorted][1] = 0

#         eggs[eggs_sort[i][0]][1] = eggs_sort[i][1]
#         eggs[left][1] = eggs_sort[left_in_sorted][1]
#         break
        

# for tc in range(1, 9 + 1):
#     answer = 0

#     eggs = []
#     eggs_sort = []
#     N = int(input())
#     for i in range(N):
#         Si, Wi = map(int, input().split())
#         eggs.append([i, Si, Wi])
#         eggs_sort.append([i, Si, Wi])
#     eggs_sort = sorted(eggs_sort, key = lambda x:(x[1], -x[2]), reverse = True)

#     for i in range(N):
#         if eggs[i][1] > 0:
#             attack(i)

#     for i, s, w in eggs:
#         if s == 0:
#             answer += 1

#     print(answer)

# # 3
# # 2
# # 0
# # 4
# # 6
# # 3
# # 3
# # 8
# # 0SSSS