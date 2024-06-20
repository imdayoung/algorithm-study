answer = 0

str1 = ' ' + input()
str2 = ' ' + input()

n, m = len(str1), len(str2)

table = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:
            table[i][j] = table[i - 1][j - 1] + 1

    answer = max(answer, max(table[i]))

print(answer)