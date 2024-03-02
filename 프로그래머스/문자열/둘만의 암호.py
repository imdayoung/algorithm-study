def solution(s, skip, index):
    answer = ''
    
    for char in s:
        i = 0
        temp = char
        
        while i < index:
            temp = chr(ord(temp) + 1)
            if ord(temp) > 122:
                temp = chr(ord(temp) - 26)
            if temp not in skip:
                i += 1
        answer += temp
        
    return answer