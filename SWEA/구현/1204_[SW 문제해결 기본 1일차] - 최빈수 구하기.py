T = int(input())
for _ in range(1, T + 1):
    tc = int(input())
    
    ans = {}
    score = list(map(int, input().split()))
    score.sort(reverse = True)
    for s in score:
        if s not in ans:
            ans[s] = 1
        else:
            ans[s] += 1
    
    most_value = 0
    for k in ans:
        if ans[k] > most_value:
            most_value = ans[k]
            answer = k
    print(f"#{tc} {answer}")