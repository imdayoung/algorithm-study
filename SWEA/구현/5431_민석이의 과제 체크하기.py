T = int(input())
for tc in range(1, T + 1):
    answer = []
    N, K = map(int, input().split())
    submitted = list(map(int, input().split()))
    for i in range(1, N + 1):
        if i not in submitted:
            answer.append(i)

    print(f"#{tc}", end = " ")
    print(*answer)