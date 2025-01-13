import sys


answer = 0

N = int(sys.stdin.readline())
plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plans.sort(key = lambda x : (x[0], x[0] - x[1]))
M = 365

calendar = [[0 for _ in range(M + 1)] for _ in range(N)]
for start, end in plans:
    for i in range(N):
        if calendar[i][start] == 0:
            for j in range(start, end + 1):
                calendar[i][j] = 1
            break
    
width, height = 0, 0
for j in range(plans[0][0], M + 1):
    flag = False
    
    for i in range(N):
        if calendar[i][j] == 1:
            flag = True
            height = max(height, i + 1)
    
    if not flag:
        answer += width * height
        width = 0
        height = 0
    else:
        width += 1
        
answer += width * height

print(answer)
