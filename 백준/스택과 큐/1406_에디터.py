import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

# 입력할 명령어의 개수
m = int(input())
for _ in range(m):
    cmd = input().rstrip()
    if cmd == "L":
        if left:
            right.append(left.pop())
    elif cmd == "D":
        if right:
            left.append(right.pop())
    elif cmd == "B":
        if left:
            left.pop()
    else:
        left.append(cmd.split()[1])

for l in left:
    print(l, end = '')
for r in right[::-1]:
    print(r, end = '')