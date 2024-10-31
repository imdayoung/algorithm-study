N, L = map(int, input().split())

for n in range(L, 101):
    x = (2 * N - n * n - n) / (2 * n)
    if x == int(x) and int(x) >= -1:
        x = int(x)
        print(*[i for i in range(x + 1, x + n + 1)])
        exit()

print(-1)
