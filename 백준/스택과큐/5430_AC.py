from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스의 개수
t = int(input().rstrip())

for _ in range(t):
    flag = 0
    reverse = 0
    p = input().rstrip()
    n = int(input().rstrip())
    x = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        x = deque()
    
    for i in p:
        if i == "R":
            reverse += 1
        elif i == "D":
            if len(x) == 0:
                flag = 1
                print("error")
                break
            else:
                if reverse % 2 == 0:
                    x.popleft()
                else:
                    x.pop()
    if flag == 0:
        if reverse % 2 == 0:
            print('['+','.join(x)+']')
        else:
            x.reverse()
            print('['+','.join(x)+']')
    