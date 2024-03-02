T = 10
for tc in range(1, T + 1):
    N = int(input())    # 원본 암호문의 길이
    password = input()  # 원본 암호문
    M = int(input())    # 명령어의 개수
    cmd = input()       # 명령어

    password = password.split()

    cmd = cmd.split("I")
    for i in range(1, len(cmd)):
        temp = cmd[i].split()

        for j in range(2, int(temp[1]) + 2):
            password.insert(int(temp[0]) + j - 2, temp[j])

    answer = [int(password[i]) for i in range(10)]
    print(f'#{tc}', end = " ")
    print(*answer)