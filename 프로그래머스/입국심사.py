def solution(n, times):
    answer = 0
    start = min(times)
    end = n * max(times) // 2 + 1

    while start <= end:
        mid = (start + end) // 2


    return answer


print(solution(6, [7, 10]))
# 28