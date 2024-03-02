# 3
# abd*dafs
# abdabcdefgdafs
# afdbsdaf
# abddafs

import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()
x = pattern.split("*")

for _ in range(n):
    word = input().rstrip()
    if len(x[0]) + len(x[1]) > len(word):
        print("NE")
        continue

    if word[:len(x[0])] == x[0] and word[-len(x[1]):] == x[1]:
        print("DA")
    else:
        print("NE")