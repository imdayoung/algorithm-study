def solution(sequence, k):
    answer = []
    
    start, end = 0, 0
    total = sequence[0]
    n = len(sequence)
    
    while True:
        if start == n - 1 and end == n - 1:
            if total == k and (answer == [] or end - start < answer[1] - answer[0]):
                answer = [start, end]
            break
        
        if total == k:
            if answer == [] or end - start < answer[1] - answer[0]:
                answer = [start, end]
                    
            if end != n - 1:
                end += 1
                total += sequence[end]
            if start != n - 1:
                total -= sequence[start]
                start += 1
                
        elif total < k:
            if end != n - 1:
                end += 1
                total += sequence[end]
            else:
                break
                
        elif total > k:
            if start != n - 1:
                total -= sequence[start] 
                start += 1

    return answer