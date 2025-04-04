import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
flag = False
answer = ""

for char in s:
    if char == " ":
        while stack:
            answer += stack.pop()
        answer += char
    elif char == "<":
        while stack:
            answer += stack.pop()
        flag = True
        answer += char
    elif char == ">":
        flag = False
        answer += char
    elif flag:
        answer += char
    else:
        stack.append(char)

while stack:
    answer += stack.pop()
    
print(answer)