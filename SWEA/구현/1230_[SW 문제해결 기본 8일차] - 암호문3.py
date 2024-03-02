T = 10
for tc in range(1, T + 1):
    N = int(input())
    codes = list(map(int, input().split()))
    M = int(input())
    command = list(map(str, input().split()))
    cnt = len(command)

    i = 0
    while i < cnt:
        if command[i] == "I":
            x = int(command[i + 1])
            y = int(command[i + 2])
            i += 3
            for _ in range(y):
                codes.insert(x, int(command[i]))
                x += 1
                i += 1
        elif command[i] == "D":
            x = int(command[i + 1])
            y = int(command[i + 2])
            i += 3
            for _ in range(y):
                del codes[x]
        elif command[i] == "A":
            y = int(command[i + 1])
            i += 2
            for _ in range(y):
                codes.append(command[i])
                i += 1

    print(f"#{tc}", end = " ")
    print(*codes[:10])