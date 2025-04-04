bracket = input()

stack = []
temp = 1
answer = 0

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
        temp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        temp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i - 1] == "(":
            answer += temp
        stack.pop()
        temp //= 2
        
    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i - 1] == "[":
            answer += temp
        stack.pop()
        temp //= 3

# 마지막 괄호가 짝이 맞지 않는 경우 대비
if stack:
    answer = 0
print(answer)