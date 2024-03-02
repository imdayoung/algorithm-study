import sys
from itertools import combinations


def DFS(n, arr):
    global answer
    if n == change:
        answer = max(answer, int(''.join([str(i) for i in arr])))
        return
    
    for i in range(len(comb)):
        a, b = comb[i]
        arr2 = arr.copy()
        arr2[a], arr2[b] = arr2[b], arr2[a]
        DFS(n + 1, arr2)
        
sys.stdin = open("input.txt", "r")

tc = int(input())
for i in range(1, tc + 1):
    answer = 0
    num = []
    temp, change = map(int, input().split())
    for j in str(temp):
        num.append(int(j))
    
    comb = list(combinations([i for i in range(len(num))], 2))

    
    DFS(0, num[::])

    print("#{} {}".format(i, answer))