N, r, c = map(int, input().split())

count = 0
while N != 0:
    N -= 1
    boundary = 2 ** N

    # 왼쪽 위 사분면
    if r < boundary and c < boundary:
        count += 0

    # 오른쪽 위 사분면
    elif r < boundary and c >= boundary:
        count += (2 ** N) * (2 ** N)
        c -= 2 ** N

    # 왼쪽 아래 사분면
    elif r >= boundary and c < boundary:
        count += (2 ** N) * (2 ** N) * 2
        r -= 2 ** N

    # 오른쪽 아래 사분면
    elif r >= boundary and c >= boundary:
        count += (2 ** N) * (2 ** N) * 3
        r -= 2 ** N
        c -= 2 ** N

print(count)