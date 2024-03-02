import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

expression = input().rstrip().split("-")

for i in range(len(expression)):
    expression[i] = expression[i].split("+")
    for j in range(len(expression[i])):
        expression[i][j] = int(expression[i][j])

answer = sum(expression[0])
for i in range(1, len(expression)):
    temp = sum(expression[i])
    answer -= temp
    
print(answer)