import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # L분 이상 U분 이하, 이번 주 X분
    L, U, X = map(int, input().split())
    if X > U:
        answer = -1
    elif X < L:
        answer = L - X
    else:
        answer = 0
    print(f"#{tc} {answer}")