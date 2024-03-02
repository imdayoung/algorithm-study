from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = 0
    tangerine = sorted(Counter(tangerine).items(), key = lambda x:x[1], reverse = True)
    
    for i in range(len(tangerine)):
        count += tangerine[i][1]
        answer += 1
        if count >= k:
            break
    
    return answer