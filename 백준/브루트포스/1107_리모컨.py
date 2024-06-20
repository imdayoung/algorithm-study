import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
start = 100
res = abs(N - start)

if M > 0:
    button_error = list(map(str, input().split()))
    if N == start:
        print(0)
    else:
        for i in range(1000001):
            i_str = str(i)
            for j in str(i):
                if j in button_error:
                    break
            else:
                res = min(res, len(i_str) + abs(i - N))

        print(res)
else:
    print(min(res, len(str(N))))