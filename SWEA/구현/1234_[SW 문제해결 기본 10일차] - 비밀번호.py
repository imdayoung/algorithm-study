T = 10
for tc in range(1, T + 1):
    
    N, temp = map(int, input().split())
    number = []
    for i in str(temp):
        number.append(i)

    while True:
        for i in range(len(number) - 1):
            if number[i] == number[i + 1]:
                del number[i]
                del number[i]
                break
        else:
            break

    print(f"#{tc} {int(''.join(i for i in number))}")