import sys


answer = 0
red_right_answer = 0
red_left_answer = 0
blue_right_answer = 0
blue_left_answer = 0
red, blue = [], []

N = int(sys.stdin.readline())
balls = list(map(str, sys.stdin.readline().rstrip()))

for i in range(N - 1, -1, -1):
    if balls[i] == 'R':
        red.append(i)
    elif balls[i] == 'B':
        blue.append(i)

red_rev = red[::-1]
blue_rev = blue[::-1]

r = len(red)
b = len(blue)

# 한 종류만 주어지는 경우
if r == 0 or b == 0:
    answer = 0
else:
    # 빨간색 공을 오른쪽으로 옮기는 경우
    if red[0] != N - 1:
        red_right_answer += 1
        red[0] = N - 1
        
    for i in range(1, r):
        if red[i - 1] - red[i] != 1:
            red_right_answer += 1
            red[i] = red[i - 1] - 1
    
    # 빨간색을 왼쪽으로 옮기는 경우
    if red_rev[0] != 0:
        red_left_answer += 1
        red_rev[0] = 0
        
    for i in range(1, r):
        if red_rev[i] - red_rev[i - 1] != 1:
            red_left_answer += 1
            red_rev[i] = red_rev[i - 1] - 1

    # 파란색 공을 오른쪽으로 옮기는 경우
    if blue[0] != N - 1:
        blue_right_answer += 1
        blue[0] = N - 1
        
    for i in range(1, b):
        if blue[i - 1] - blue[i] != 1:
            blue_right_answer += 1
            blue[i] = blue[i - 1] - 1
    
    # 파란색을 왼쪽으로 옮기는 경우
    if blue_rev[0] != 0:
        blue_left_answer += 1
        blue_rev[0] = 0
        
    for i in range(1, b):
        if blue_rev[i] - blue_rev[i - 1] != 1:
            blue_left_answer += 1
            blue_rev[i] = blue_rev[i - 1] - 1
        
print(min(red_right_answer, red_left_answer, blue_right_answer, blue_left_answer))
