def solution(n, times):
    start = min(times)
    end = n * max(times)
    answer = end

    while start <= end:
        mid = (start + end) // 2
        people = 0
        # mid분 동안 한 명의 심사관이 심사할 수 있는 사람의 수
        for time in times:
            people += mid // time
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(6, [7, 10]))
# 28