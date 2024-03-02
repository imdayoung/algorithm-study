import sys


t = int(sys.stdin.readline())
for _ in range(t):
    clothes = {}
    n = int(input())
    for _ in range(n):
        cloth_name, cloth_type = map(str, sys.stdin.readline().rstrip().split())
        if cloth_type not in clothes:
            clothes[cloth_type] = 1
        else:
            clothes[cloth_type] += 1

    result = 1
    for cnt in clothes.values():
        result *= (cnt + 1)

    print(result - 1)