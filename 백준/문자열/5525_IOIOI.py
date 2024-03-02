import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

answer = 0
i = 0
count = 0

while i < M - 1:
    if S[i:i + 3] == "IOI":
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)