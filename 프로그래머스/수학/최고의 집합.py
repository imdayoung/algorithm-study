def solution(n, s):  
    num = s // n
    rem = s % n
    
    if num < 1:
        return [-1]
    
    answer = [num for _ in range(n)]
    i = n - 1
    while rem > 0:
        answer[i] += 1
        i -= 1
        rem -= 1
    
    return answer