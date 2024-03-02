def find_near(a, b):
    a_near, b_near = -1, -1
    for i in range(0, 21):
        if a_near == -1 and 2 ** i >= a:
            a_near = i
        if b_near == -1 and 2 ** i >= b:
            b_near = i
        if a_near > -1 and b_near > -1:
            break
    return a_near, b_near


def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
        
    a_near, b_near = find_near(a, b)
    if a_near != b_near:
        return b_near
    else:
        while a_near == b_near:
            n = a_near - 1
            a -= 2 ** n
            b -= 2 ** n
            a_near, b_near = find_near(a, b)
        return b_near