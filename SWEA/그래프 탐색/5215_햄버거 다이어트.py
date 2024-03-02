def dfs(idx, sum_floavor, sum_calorie):
    global max_flavor
    # 칼로리 초과하면 리턴
    if sum_calorie > L:
        return
    
    # 최고 맛 점수보다 높으면 갱신
    if max_flavor < sum_floavor:
        max_flavor = sum_floavor

    # 마지막 재료 확인 후 리턴
    if idx == N:
        return
    
    flavor, calorie = ingredients[idx]
    # 재료를 사용했을 때
    dfs(idx + 1, sum_floavor + flavor, sum_calorie + calorie)
    # 재료를 사용하지 않았을 때
    dfs(idx + 1, sum_floavor, sum_calorie)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    max_flavor = 0
    dfs(0, 0, 0)
    print(f"#{tc} {max_flavor}")