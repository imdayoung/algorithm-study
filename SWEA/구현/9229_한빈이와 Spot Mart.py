TC = int(input())
for tc in range(1, TC + 1):
    snack = []

    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    weight.sort()
    for i in range(len(weight) - 1):
        for j in range(i + 1, len(weight)):
            temp = weight[i] + weight[j]
            if temp <= M:
                snack.append(temp)

    if len(snack):
        print(f'#{tc} {max(snack)}')
    else:
        print(f'#{tc} -1')