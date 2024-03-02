import sys
input = sys.stdin.readline

def cmd_1():
    global arr
    arr = arr[::-1]
    

def cmd_2():
    global arr
    for i in range(N):
        arr[i] = arr[i][::-1]


def cmd_3():
    global arr
    temp = []
    for i in range(M):
        temp.append([a[i] for a in arr][::-1])
    arr = temp


def cmd_4():
    global arr
    temp = []
    for i in range(M - 1, -1, -1):
        temp.append([a[i] for a in arr])
    arr = temp

    
def cmd_5():
    global arr
    group_1 = divide_four(arr, 0, 0)
    group_2 = divide_four(arr, 0, M // 2)
    group_3 = divide_four(arr, N // 2, 0)
    group_4 = divide_four(arr, N // 2, M // 2)
    temp = []
    for i in range(N // 2):
        temp.append(group_3[i] + group_1[i])
    for i in range(N // 2):
        temp.append(group_4[i] + group_2[i])
    arr = temp

    
def cmd_6():
    global arr
    group_1 = divide_four(arr, 0, 0)
    group_2 = divide_four(arr, 0, M // 2)
    group_3 = divide_four(arr, N // 2, 0)
    group_4 = divide_four(arr, N // 2, M // 2)
    temp = []
    for i in range(N // 2):
        temp.append(group_2[i] + group_4[i])
    for i in range(N // 2):
        temp.append(group_1[i] + group_3[i])
    arr = temp


def divide_four(graph, x, y):
    divided_graph = []
    for i in range(x, x + N // 2):
        temp = []
        for j in range(y, y + M // 2):
            temp.append(graph[i][j])
        divided_graph.append(temp)
    return divided_graph


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

for cmd in cmds:
    if cmd == 1:
        cmd_1()
    elif cmd == 2:
        cmd_2()
    elif cmd == 3:
        cmd_3()
        N, M = M, N
    elif cmd == 4:
        cmd_4()
        N, M = M, N
    elif cmd == 5:
        cmd_5()
    elif cmd == 6:
        cmd_6()

for a in arr:
    print(*a)