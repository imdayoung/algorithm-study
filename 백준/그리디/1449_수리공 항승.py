import sys


answer = 1

N, L = map(int, sys.stdin.readline().split())
locations = list(map(int, sys.stdin.readline().split()))
locations.sort()

start, end = locations[0] - 0.5, locations[0] - 0.5 + L
for loc in locations:
    if loc + 0.5 > end:
        start = loc - 0.5
        end = start + L
        answer += 1
        
print(answer)
