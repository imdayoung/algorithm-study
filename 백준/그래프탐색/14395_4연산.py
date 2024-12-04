import sys
from collections import deque


def bfs(num):
    queue = deque([[num, ""]])
    visited = set()
    visited.add(num)
    
    while queue:
        n, calculator = queue.popleft()
        if n == t:
            return calculator
        
        if n * n <= t and n * n not in visited:
            visited.add(n * n)
            queue.append([n * n, calculator + "*"])
        if n + n <= t and n + n not in visited:
            visited.add(n + n)
            queue.append([n + n, calculator + "+"])
        if 0 not in visited:
            visited.add(0)
            queue.append([0, calculator + "-"])
        if n != 0 and 1 not in visited:
            visited.add(1)
            queue.append([1, calculator + "/"])
            
    return -1
    

s, t = map(int, sys.stdin.readline().split())
if s == t:
    print(0)
else:
    calculators = bfs(s)
    print(calculators)
