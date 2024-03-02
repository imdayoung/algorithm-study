T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(M)]
    sum_arr = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1]  - sum_arr[i - 1][j - 1] + flies[i - 1][j - 1]

    answer = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            catch = sum_arr[i + M][j + M] - sum_arr[i + M][j] - sum_arr[i][j + M] + sum_arr[i][j]
            if catch > answer:
                answer = catch
        
    print(f"#{tc} {answer}")