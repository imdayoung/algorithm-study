import sys


N = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

works.sort(key = lambda x:-x[1])
print(works)

timeline = [0 for _ in range(24)]
cur_time = works[0][1] - 1

for work in works:
    print(work, cur_time)
    long = work[0]
    deadline = work[1]
    
    if long >= cur_time:
        answer = -1
        break
    
    cur_time -= long
    answer = cur_time
    
print(answer)