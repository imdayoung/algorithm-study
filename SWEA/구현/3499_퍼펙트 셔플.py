T = int(input())
for tc in range(1, T + 1):
    answer = []
    
    N = int(input())
    cards = list(map(str, input().split()))
    cards_1 = cards[:N // 2 + N % 2]
    cards_2 = cards[N // 2 + N % 2:]

    for i in range(N // 2):
        answer.append(cards_1[i])
        answer.append(cards_2[i])
    if N % 2 == 1:
        answer.append(cards_1[-1])
    print(f"#{tc}", end = " ")
    print(*answer) 