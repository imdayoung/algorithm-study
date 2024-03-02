import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
i = 1

for _ in range(n):
    num = int(input())
    while i <= num:
        stack.append(i)
        answer.append("+")
        i += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        break
else:
    for a in answer:
        print(a)