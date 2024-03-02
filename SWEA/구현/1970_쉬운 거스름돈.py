import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    money = int(input())

    cnt_50000 = money // 50000
    money %= 50000
    cnt_10000 = money // 10000
    money %= 10000
    cnt_5000 = money // 5000
    money %= 5000
    cnt_1000 = money // 1000
    money %= 1000
    cnt_500 = money // 500
    money %= 500
    cnt_100 = money // 100
    money %= 100
    cnt_50 = money // 50
    money %= 50
    cnt_10 = money // 10

    print(f"#{tc}")
    print(cnt_50000, cnt_10000, cnt_5000, cnt_1000, cnt_500, cnt_100, cnt_50, cnt_10)