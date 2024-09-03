T = int(input())
for tc in range(1, T + 1):
    # 재료의 수 N, 제한 칼로리 L
    N, L = map(int, input().split())
    ingredients = [[0, 0]]
    dp = [[0] * (L + 1) for _ in range(N + 1)]

    # 재로에 대한 점수와 칼로리 리스트에 저장
    for _ in range(N):
        score, calorie = map(int, input().split())
        ingredients.append([score, calorie])

    for i in range(N + 1):
        for j in range(L + 1):
            score = ingredients[i][0]
            calorie = ingredients[i][1]

            if j < calorie:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - calorie] + score, dp[i - 1][j])

    print(f'#{tc} {dp[N][L]}')