import sys
input = sys.stdin.readline

s = set()
m = int(input())
for _ in range(m):
    cmd = input().rstrip().split()

    if len(cmd) == 1:
        if cmd[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    
    command, target = cmd[0], int(cmd[1])
    if command == "add":
        if target not in s:
            s.add(target)
    elif command == "remove":
        if target in s:
            s.remove(target)
    elif command == "check":
        if target in s:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if target in s:
            s.remove(target)
        else:
            s.add(target)