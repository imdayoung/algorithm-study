import sys


def hanoi(n, start, assist, end):
    if n == 0:
        return
    
    hanoi(n - 1, start, end, assist)
    print(start, end)
    hanoi(n - 1, assist, start, end)

N = int(sys.stdin.readline())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)