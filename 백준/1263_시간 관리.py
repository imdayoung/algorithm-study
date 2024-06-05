import sys


N = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

works.sort(key = lambda x:(-x[1], -x[0]))
# print(works)

cur_time = works[0][1]

for work in works:
    # print(work, cur_time)
    duration = work[0]
    deadline = work[1]
    
    if duration > cur_time:
        answer = -1
        break
    
    if deadline < cur_time:
        cur_time = deadline - duration
    else:
        cur_time -= duration
        
    answer = cur_time
    
print(answer)