import heapq


N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    a[i] = -a[i]    
heapq.heapify(a)

time = 0
for _ in range(1440):
    if len(a) > 0:
        h1 = heapq.heappop(a)
    else:
        break
    
    if len(a) > 0:
        h2 = heapq.heappop(a)
        if h2 < -1:
            heapq.heappush(a, h2 + 1)
            
    if h1 < -1:
        heapq.heappush(a, h1 + 1)
    
    time += 1
    
if sum(a) != 0:
    print(-1)
else:
    print(time)
