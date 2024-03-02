def solution(s):
    stack = []
    
    for char in s:
        stack.append(char)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            
    return 0 if stack else 1