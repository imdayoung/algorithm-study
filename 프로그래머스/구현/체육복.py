def solution(n, lost, reserve):
    answer = n - len(lost)
    lost, reserve = sorted(lost), sorted(reserve)
    
    for i in lost:
        if i in reserve:
            answer += 1
            reserve.remove(i)
        elif i - 1 in reserve and i - 1 not in lost:
            answer += 1
            reserve.remove(i - 1)  
        elif i + 1 in reserve and i + 1 not in lost:
            answer += 1
            reserve.remove(i + 1)
        
    return answer