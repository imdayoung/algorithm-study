str1 = ' ' + input()
str2 = ' ' + input()

x = len(str1)
y = len(str2)

table = [[0] * y for _ in range(x)]

for i in range(1, x):
    for j in range(1, y):
        if str1[i] == str2[j]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

print(table[-1][-1])