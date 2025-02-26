import sys
import heapq


n = int(sys.stdin.readline())
presents = []

for _ in range(n):
    charge = list(map(int, sys.stdin.readline().rstrip().split()))
    a = charge[0]
    
    if a == 0:
        if len(presents) == 0:
            print(-1)
        else:
            give = heapq.heappop(presents)
            print(-give)
    else:
        charge = charge[1:]
        for c in charge:
            heapq.heappush(presents, -c)
