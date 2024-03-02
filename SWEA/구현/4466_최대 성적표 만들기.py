T = int(input())
for tc in range(1, T + 1):
    answer = 0

    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse = True)
    
    for i in range(K):
        answer += score[i]

    print(f"#{tc} {answer}")