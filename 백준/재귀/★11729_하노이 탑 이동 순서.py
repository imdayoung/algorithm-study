import sys
sys.setrecursionlimit(10 ** 6)

def hanoi(n, start, end, assist):
    if n == 0:
        return
    hanoi(n - 1, start, assist, end)
    print(start, end)
    hanoi(n - 1, assist, end, start)


N = int(sys.stdin.readline())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)