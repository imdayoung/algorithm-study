def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        count = 0
        prev_rock = 0
        
        for rock in rocks:
            # 간격이 최소간격 mid보다 작으면 -> 존재하면 안됐던 바위 -> 제거
            if rock - prev_rock < mid:
                count += 1
                if count > n:
                    break
                
            # 바위를 제거하지 않아도 되는 경우
            else:
                prev_rock = rock
                
        if count <= n:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    
    return answer