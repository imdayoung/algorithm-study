import sys


answer = 0

MAX = 0
N, K = map(int, sys.stdin.readline().split())
ices = [0 for _ in range(1000000)]
for _ in range(N):
    g, x = map(int, sys.stdin.readline().split())
    ices[x] = g
    MAX = max(MAX, x)

if K > 1000000:
    print(sum(ices))
    exit()

start, end = 0, 2 * K

for i in range(start, end + 1):
    answer += ices[i]

temp = answer
while end <= MAX:
    temp -= ices[start]
    start += 1
    
    end += 1
    if end > MAX - 1:
        continue
    temp += ices[end]
    
    answer = max(answer, temp)

print(answer)
