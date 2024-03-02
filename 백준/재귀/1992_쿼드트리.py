import sys
input = sys.stdin.readline

def div(n, x, y):
    temp = video[x][y]
    flag = 0
    # 구역 안의 숫자가 모두 같은 지 확인
    # 0과 1이 섞여 있으면 flag -1
    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != temp:
                flag = -1
                break
        if flag == -1:
            break
    
    # 구역에 0과 1이 섞여 있는 경우
    if flag == -1:
        print("(", end = "")
        div(n // 2, x, y)
        div(n // 2, x, y + n // 2)
        div(n // 2, x + n // 2, y)
        div(n // 2, x + n // 2, y + n // 2)
        print(")", end = "")

    # 구역이 모두 0 또는 1로 이루어져 분할할 필요 없는 경우
    else:
        print(temp, end = "")

N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N)]
div(N, 0, 0)