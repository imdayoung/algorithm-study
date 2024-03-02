T = int(input())
for tc in range(1, T + 1):
    answer = 1
    check = []
    t = {"S":13, "D":13, "H":13, "C":13}

    cards = input()
    for i in range(0, len(cards), 3):
        card = cards[i:i + 3]
        if card in check:
            answer = "ERROR"
            break
        else:
            t[card[0]] -= 1
            check.append(card)

    if answer == 1:
        print(f"#{tc}", end = " ")
        print(*t.values())
    else:
        print(f"#{tc} {answer}")    