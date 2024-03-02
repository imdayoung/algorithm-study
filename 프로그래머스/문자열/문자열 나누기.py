def solution(s):
    answer = 0
    start = s[0]
    start_num, not_start_num = 0, 0
    
    for i in range(len(s)):
        if s[i] == start:
            start_num += 1
        else:
            not_start_num += 1
        
        if start_num == not_start_num:
            answer += 1
            print(start, start_num, not_start_num)
            if i + 1 < len(s):
                start = s[i + 1]
                start_num, not_start_num = 0, 0
                
        if i == len(s) - 1 and start_num != not_start_num:
                answer += 1
    return answer