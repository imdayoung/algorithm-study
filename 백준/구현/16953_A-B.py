import sys

count = 0
A, B = map(int, sys.stdin.readline().split())

while B != A:
    if len(str(B)) > 1 and str(B)[-1] == "1":
        B = int(str(B)[:-1])
    elif B % 2 == 0:
        B = B // 2
    else:
        count = -2
        break
    count += 1

print(count + 1)