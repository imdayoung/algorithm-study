import sys


R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]

words = []

# 가로 단어 확인
for i in range(R):
    temp = ""
    for j in range(C):
        alphabet = board[i][j]
        if alphabet == '#':
            if len(temp) > 1:
                words.append(temp)
            temp = ""
        else:
            temp += alphabet
    if len(temp) > 1:
        words.append(temp)

# 세로 단어 확인
for j in range(C):
    temp = ""
    for i in range(R):
        alphabet = board[i][j]
        if alphabet == '#':
            if len(temp) > 1:
                words.append(temp)
            temp = ""
        else:
            temp += alphabet
    if len(temp) > 1:
        words.append(temp)            

words.sort()
print(words[0])
