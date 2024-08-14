import sys


answer = 0

N, K = map(int, sys.stdin.readline().split())
levels = list(int(sys.stdin.readline()) for _ in range(N))

start = min(levels)
end = max(levels) + K

while end >= start:
    mid = (start + end) // 2
    need = 0
    
    for level in levels:
        if level < mid:
            need += mid - level
        
    if need > K:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
        
        
print(answer)
    

# # 시간 초과
# import sys
# import heapq


# N, K = map(int, sys.stdin.readline().split())
# levels = list(int(sys.stdin.readline()) for _ in range(N))
# heapq.heapify(levels)

# for _ in range(K):
#     heapq.heappush(levels, heapq.heappop(levels) + 1)
        
# print(heapq.heappop(levels))
