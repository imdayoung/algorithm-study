# 올바른 괄호 문자열인지 판별
def is_right_bracket(w):
    stack = []
    for i in range(len(w)):
        b = w[i]
        if b == "(":
            stack.append(b)
        else:
            if not stack or stack[-1] == ")":
                return False
            stack.pop()

    if stack:
        return False
    return True


# 문자열 분리
def split_string(w):
    if w == '':
        return ''
    
    left, right = 0, 0
    
    for i in range(0, len(w)):
        if w[i] == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            return [w[:i + 1], w[i + 1:]]


def make_right_bracket(w):
    answer = ''

    # 1. 입력이 빈 문자열인 경우 빈 문자열 반환
    if len(w) == 0:
        return ''
    
    # 2. 문자열 w를 균형잡힌 괄호 문자열 u, v로 분리
    u, v = split_string(w)

    # 3. 문자열 u가 올바른 괄호 문자열인 경우
    if is_right_bracket(u):
        return u + make_right_bracket(v)

    # 4. 문자열 u가 올바른 괄호 문자열이 아닌 경우
    else:
        answer = "("
        answer += make_right_bracket(v)
        answer += ")"
        for char in u[1:len(u) - 1]:
            if char == ")":
                answer += "("
            else:
                answer += ")"
        return answer


def solution(p):
    return make_right_bracket(p)