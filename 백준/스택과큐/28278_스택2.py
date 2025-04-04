import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []

for i in range(n):
    cmd = input().rstrip()
    if cmd[0] == "1":
        num = int(cmd.split()[1])
        stack.append(num)
    elif cmd == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "3":
        print(len(stack))
    elif cmd == "4":
        num = 0 if stack else 1
        print(num)
    elif cmd == "5":
        num = stack[-1] if stack else -1
        print(num)