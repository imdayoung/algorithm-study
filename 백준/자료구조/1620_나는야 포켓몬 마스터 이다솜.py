import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
pocketmon_number = {}
pocketmon_name = {}

for i in range(n):
    name = input().rstrip()
    pocketmon_number[i + 1] = name
    pocketmon_name[name] = i + 1

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(pocketmon_number[int(a)])
    else:
        print(pocketmon_name[a])