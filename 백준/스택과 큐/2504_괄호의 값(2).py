import sys


answer = 0
temp = 1
stack = []

brackets = sys.stdin.readline().rstrip()
n = len(brackets)

for i in range(n):
    cur = brackets[i]
    
    if cur == '(':
        temp *= 2
        stack.append(cur)

    elif cur == ')':
        # 잘못된 괄호열
        if not stack or stack[-1] != '(':
            answer = 0
            break

        if brackets[i - 1] == '(':
            answer += temp

        stack.pop()
        temp //= 2

    elif cur == '[':
        temp *= 3
        stack.append(cur)

    elif cur == ']':
        # 잘못된 괄호열
        if not stack or stack[-1] != '[':
            answer = 0
            break
        
        if brackets[i - 1] == '[':
            answer += temp

        stack.pop()
        temp //= 3

    else:
        answer = 0
        break
    
if stack:
    answer = 0

print(answer)