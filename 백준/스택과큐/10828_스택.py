n = int(input())
stack = []

for _ in range(n):
    cmd_line = input()
    cmd = cmd_line.split()[0]
    if cmd == "push":
        stack.append(cmd_line.split()[1])
    elif cmd == "pop":
        if stack:
            num = stack.pop()
            print(num)
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        num = 0 if stack else 1
        print(num)
    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)