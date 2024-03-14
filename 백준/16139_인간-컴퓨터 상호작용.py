import sys


S = sys.stdin.readline()
q = int(sys.stdin.readline())

for _ in range(q):
    alphabet, l, r = map(str, sys.stdin.readline().split())
    l = int(l)
    r = int(r)


# 각 알파벳에 대한 누적합 ..?

# # 50점따리
# from collections import Counter
# import sys


# S = sys.stdin.readline()
# q = int(sys.stdin.readline())
# for _ in range(q):
#     alphabet, l, r = map(str, sys.stdin.readline().split())
#     l = int(l)
#     r = int(r)

#     dict = {}
#     counter = Counter(S[l:r + 1]).items()
#     for key, value in counter:
#         dict[key] = value

#     if alphabet not in dict:
#         print(0)
#     else:
#         print(dict[alphabet])