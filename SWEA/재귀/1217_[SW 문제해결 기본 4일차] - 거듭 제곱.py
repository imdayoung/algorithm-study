def square(n, m, res):
    if m > 0:
        res = res * n
        return square(n, m - 1, res)
    else:
        return res

for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    answer = square(N, M, 1)
    print(f'#{tc} {answer}')