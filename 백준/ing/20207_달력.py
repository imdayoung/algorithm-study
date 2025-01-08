import sys

    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

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
    
# for c in calendar:
#     print(c)
    
for j in range(plans[0][0], M + 1):
    start_x, start_y = 1, 1
    end_x, end_y = 0, 0
    if calendar[0][j] == 1:
        start_x = i
        end_y = 0
        for i in range(N):
            if calendar[i][j] == 1:
                end_y = max(end_y, j)
    else:
        end_x = i
        answer += (end_x - start_x + 1) * (end_y - start_y + 1)
        
        
print(answer)
