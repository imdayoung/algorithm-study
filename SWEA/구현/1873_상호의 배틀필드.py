T = int(input())
# 위, 아래, 왼쪽, 오른쪽
for tc in range(1, T + 1):
    field = []
    # 높이 H, 너비 W
    H, W = map(int, input().split())
    # 게임 맵 입력 받고 전차의 초기 위치와 방향 찾기
    for i in range(H):
        temp = list(map(str, input().rstrip()))
        field.append(temp)
        if "^" in temp:
            x = i
            y = temp.index("^")
            direction = "^"
        elif "v" in temp:
            x = i
            y = temp.index("v")
            direction = "v"
        elif "<" in temp:
            x = i
            y = temp.index("<")
            direction = "<"
        elif ">" in temp:
            x = i
            y = temp.index(">")
            direction = ">"
    
    N = int(input())
    actions = input().rstrip()

    for action in actions:
        if action == "U":
            direction = "^"
            field[x][y] = direction
            if x - 1 > -1 and field[x - 1][y] == ".":
                field[x][y] = "."
                x -= 1
                field[x][y] = "^"
        elif action == "D":
            direction = "v"
            field[x][y] = direction
            if x + 1 < H and field[x + 1][y] == ".":
                field[x][y] = "."
                x += 1
                field[x][y] = "v"
        elif action == "L":
            direction = "<"
            field[x][y] = direction
            if y - 1 > -1 and field[x][y - 1] == ".":
                field[x][y] = "."
                y -= 1
                field[x][y] = "<"
        elif action == "R":
            direction = ">"
            field[x][y] = direction
            if y + 1 < W and field[x][y + 1] == ".":
                field[x][y] = "."
                y += 1
                field[x][y] = ">"
        elif action == "S":
            # 포탄을 발사한 방향에 벽돌 벽이 있다면 평지가 됨
            if direction == "^":
                for i in range(1, x + 1):
                    if field[x - i][y] == "#":
                        break
                    if field[x - i][y] == "*":
                        field[x - i][y] = "."
                        break
            elif direction == "v":
                for i in range(1, H - x):
                    if field[x + i][y] == "#":
                        break
                    if field[x + i][y] == "*":
                        field[x + i][y] = "."
                        break
            elif direction == "<":
                for i in range(1, y + 1):
                    if field[x][y - i] == "#":
                        break
                    if field[x][y - i] == "*":
                        field[x][y - i] = "."
                        break
            elif direction == ">":
                for i in range(1, W - y):
                    if field[x][y + i] == "#":
                        break
                    if field[x][y + i] == "*":
                        field[x][y + i] = "."
                        break
    
    print(f'#{tc}', end = " ")
    for f in field:
        for c in f:
            print(c, end = "")
        print()