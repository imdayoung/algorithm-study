from collections import deque
import sys


def D_cal(n):
    return (n * 2) % 10000


def S_cal(n):
    if n == 0:
        return 9999
    return n - 1


def L_cal(n):
    d1 = n // 1000
    d2 = (n % 1000) // 100
    d3 = (n % 100) // 10
    d4 = n % 10

    if len(str(n)) == 1:
        return int(str(d4) + "0")
    if len(str(n)) == 2:
        return int(str(d3) + str(d4) + "0")
    if len(str(n)) == 3:
        return int(str(d2) + str(d3) + str(d4) + "0")
    return int(str(d2) + str(d3) + str(d4) + str(d1))


def R_cal(n):
    d1 = n // 1000
    d2 = (n % 1000) // 100
    d3 = (n % 100) // 10
    d4 = n % 10

    if len(str(n)) == 1:
        return int(str(d4) + "000")
    if len(str(n)) == 2:
        return int(str(d4) + "00" + str(d3))
    if len(str(n)) == 3:
        return int(str(d4) + "0" + str(d2) + str(d3))
    return int(str(d4) + str(d1) + str(d2) + str(d3))


def transfrom(start, target):
    queue = deque([start])
    visited[start] = "A"

    while queue:
        num = queue.popleft()
        if num == target:
            return visited[num][1:]
        
        next_nums = [D_cal(num), S_cal(num), L_cal(num), R_cal(num)]
        for i in range(4):
            next_num = next_nums[i]
            if visited[next_num] == "":
                visited[next_num] = visited[num] + moving[i]
                queue.append(next_num)

moving = {0:"D", 1:"S", 2:"L", 3:"R"}

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [""] * 10000
    print(transfrom(A, B))