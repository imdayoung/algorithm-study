T = int(input())
for tc in range(1, T + 1):
    cnt = 0
    N, D = map(int, input().split())

    if D > N:
        cnt = 1
    else:
        i = 0
        for i in range(D, N, D * 2 + 1):
            cnt += 1
        if i + D < N - 1:
            cnt += 1
    print(f"#{tc} {cnt}")