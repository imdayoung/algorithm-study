from collections import deque


def check_bracket(bracket):
    stack = []
    for b in bracket:
        if b == "(" or b == "[" or b == "{":
            stack.append(b)
        elif b == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif b == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        elif b == "}":
            if not stack or stack[-1] != "{":
                return False
            stack.pop()
    if stack:
        return False
    return True
            

def solution(s):
    answer = 0
    queue = deque(s)
    
    for _ in range(len(s)):
        queue.append(queue.popleft())
        if check_bracket(queue):
            answer += 1
            
    return answer