import sys


def compress(n, x, y):
    global answer
    flag = graph[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != flag:
                answer += '('
                compress(n // 2, x, y)
                compress(n // 2, x, y + n // 2)
                compress(n // 2, x + n // 2, y)
                compress(n // 2, x + n // 2, y + n // 2)
                answer += ')'
                return
            
    answer += str(flag)


answer = ''
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

compress(N, 0, 0)
print(answer)