def solution(n, m, section):
    answer, i, start = 0, 0, section[0]

    for i in section:
        if i >= start:
            answer += 1
            start = i + m
            
    return answer