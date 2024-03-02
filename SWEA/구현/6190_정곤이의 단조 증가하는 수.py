T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    increasing = []
    answer = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            temp = nums[i] * nums[j]
            temp = str(temp)

            for k in range(len(temp) - 1):
                if int(temp[k]) > int(temp[k + 1]):
                    break
            else:
                increasing.append(int(temp))
    
    if len(increasing) > 0:
        answer = max(increasing)
    print(f'#{tc} {answer}')