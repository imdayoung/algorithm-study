import sys
input = sys.stdin.readline

sides = [0 for _ in range(102)]
sides[1], sides[2], sides[3] = 1, 1, 1
sides[4], sides[5] = 2, 2

for i in range(6, 101):
    sides[i] = sides[i - 1] + sides[i - 5]

t = int(input())
for _ in range(t):
    n = int(input())
    print(sides[n])