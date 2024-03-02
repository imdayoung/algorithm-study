for _ in range(10):
    answer = 0
    tc = int(input())
    target = input()
    sentence = input()
    len_target = len(target)

    while sentence.find(target) != -1 and len(sentence) > 0:
        answer += 1
        sentence = sentence[sentence.find(target) + len_target:]

    print(f'#{tc} {answer}')