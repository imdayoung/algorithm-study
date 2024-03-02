def solution(s):
    bracket = []
    for char in s:
        if char == "(":
            bracket.append(char)
        else:
            if bracket:
                bracket.pop()
            else:
                return False
    return False if bracket else True