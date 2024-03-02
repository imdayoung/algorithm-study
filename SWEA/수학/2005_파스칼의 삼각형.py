T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = [[1 for _ in range(i)] for i in range(1, N + 1)]
    for i in range(2, N):
        for j in range(1, i):
            answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

    print(f"#{tc}")
    for a in answer:
        print(*a)