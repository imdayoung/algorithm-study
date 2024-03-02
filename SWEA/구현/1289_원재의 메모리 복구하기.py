T = int(input())
for tc in range(1, T + 1):
    answer = 0
    target = list(map(int, input()))
    len_target = len(target)
    memory = [0 for _ in range(len_target)]
    
    for i in range(len_target):
        if target[i] != memory[i]:
            check = i
            break

    while target != memory:
        for i in range(check, len(target)):
            if target[i] != memory[i]:
                memory[i:] = [target[i]] * (len(target) - i)
                check = i + 1
                answer += 1
                break

    print(f'#{tc} {answer}')