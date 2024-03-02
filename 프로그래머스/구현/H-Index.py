def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for idx, val in enumerate(citations):
        if idx >= val:
            return idx
    return len(citations)