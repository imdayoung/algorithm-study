import sys


answer = 0
N, K = map(int, sys.stdin.readline().split())

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if str(K) in time:
                answer += 1

print(answer)
