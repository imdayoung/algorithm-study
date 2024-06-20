import sys


answer = 0

N, d, k, c = map(int, sys.stdin.readline().split())
sushi_on_belt = [int(sys.stdin.readline()) for _ in range(N)]
sushi_on_belt.extend(sushi_on_belt)

for i in range(N):
    answer = max(answer, len(set(sushi_on_belt[i:i + k] + [c])))
    
print(answer)
