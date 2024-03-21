import sys


answer = []
S = sys.stdin.readline().rstrip()
len_S = len(S)
q = int(sys.stdin.readline())

alphabets = [[0 for _ in range(26)] for _ in range(len_S + 1)]

for i in range(len_S):
    alphabets[i + 1][ord(S[i]) - 97] = alphabets[i][ord(S[i]) - 97] + 1
    for j in range(26):
        if j == ord(S[i]) - 97:
            continue
        alphabets[i + 1][j] = alphabets[i][j]

for _ in range(q):
    alphabet, l, r = map(str, sys.stdin.readline().split())
    a = ord(alphabet) - 97
    l = int(l)
    r = int(r)
    answer.append(alphabets[r + 1][a] - alphabets[l][a])

print(*answer, sep = "\n")


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