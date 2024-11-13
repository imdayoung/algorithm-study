import sys


def cal_1(arr):
    return arr[::-1]


def cal_2(arr):
    res = []
    for i in range(N):
        res.append(arr[i][::-1])
    return res


def cal_3(arr):
    res = []
    for j in range(M):
        temp = [arr[i][j] for i in range(N - 1, -1, -1)]
        res.append(temp)
    return res


def cal_4(arr):
    res = []
    for j in range(M - 1, -1, -1):
        temp = [arr[i][j] for i in range(N)]
        res.append(temp)
    return res


def cal_5(arr):
    res = []

    group_1, group_2, group_3, group_4 = get_group(arr)

    for i in range(N // 2):
        res.append(group_4[i] + group_1[i])
    for i in range(N // 2):
        res.append(group_3[i] + group_2[i])
    
    return res


def cal_6(arr):
    res = []

    group_1, group_2, group_3, group_4 = get_group(arr)

    for i in range(N // 2):
        res.append(group_2[i] + group_3[i])
    for i in range(N // 2):
        res.append(group_1[i] + group_4[i])
    
    return res


def get_group(arr):
    group_1, group_2, group_3, group_4 = [], [], [], []

    for i in range(N // 2):
        group_1.append(arr[i][:M // 2])
        group_2.append(arr[i][M // 2:])

    for i in range(N // 2, N):
        group_3.append(arr[i][M // 2:])
        group_4.append(arr[i][:M // 2])
        
    return group_1, group_2, group_3, group_4


N, M, R = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cals = list(map(int, sys.stdin.readline().split()))

for cal in cals:
    if cal == 1:
        A = cal_1(A)
    elif cal == 2:
        A = cal_2(A)
    elif cal == 3:
        A = cal_3(A)
    elif cal == 4:
        A = cal_4(A)
    elif cal == 5:
        A = cal_5(A)
    elif cal == 6:
        A = cal_6(A)

    N = len(A)
    M = len(A[0])

for a in A:
    print(*a)
